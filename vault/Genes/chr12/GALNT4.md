---
symbol: "GALNT4"
type: "gene"
col: 15052
ensembl_id: "ENSG00000257594"
name: "polypeptide N-acetylgalactosaminyltransferase 4"
location: "12q21.33"
module: 16
arm: "+"
pooled_cpm: 19.67
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# GALNT4

*polypeptide N-acetylgalactosaminyltransferase 4* — 12q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 1.46× (z +6.4, q 7e-08, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.503× (z -8.6, q 6e-15, down in 31 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.634× (z -7.8, q 3e-12, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM15]] (+0.55, fdr 2e-05), [[BZW1]] (+0.54, fdr 1e-05), [[WDCP]] (+0.51, fdr 4e-04); moves opposite to [[GOLGA6L9]] (-0.52, fdr 1e-05), [[GUCA1B]] (-0.50, fdr 1e-05), [[PPP2R2D]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SERPINB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15052.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +6.4 | 7e-08 | 24/48 (LS 180, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.31× | +3.4 | 0.18 | 11/48 (HOP62, A-427, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.29× | +3.2 | 0.24 | 9/48 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -8.6 | 6e-15 | 31/46 (Hs 766T, H4, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.634×** | -7.8 | 3e-12 | 27/46 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.553×** | -7.4 | 3e-11 | 33/48 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.596×** | -6.5 | 2e-08 | 28/46 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.608×** | -4.4 | 9e-04 | 27/44 (SNU-1, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.701×** | -4.4 | 9e-04 | 20/47 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.688×** | -4.4 | 9e-04 | 20/46 (KATO III, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -4.2 | 0.002 | 17/43 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.716×** | -4.0 | 0.004 | 21/47 (AsPC-1, COLO 205, …) | top dose only | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.729×** | -3.9 | 0.005 | 18/47 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.671×** | -3.5 | 0.020 | 14/47 (SHP-77, CHP-212, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.824×** | -3.3 | 0.047 | 17/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | **0.831×** | -3.1 | 0.072 | 12/48 (HOP62, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.778×** | -3.1 | 0.072 | 15/47 (NCI-H460, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 56.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 46.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -15.9) |
| [[COLO 205 (line)]] | alt | 38.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -14.1) |
| [[KATO III (line)]] | alt | 72.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 38.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.4) |
| [[H4 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -8.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.3) |
| [[SW 900 (line)]] | alt | 44.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -11.3) |
| [[SW48 (line)]] | wt | 12.4 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0829× (z -9.2) |
| [[A-172 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM15]] | +0.55 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[BZW1]] | +0.54 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[WDCP]] | +0.51 | +0.26 / +0.46 | both halves | 4e-04 |  |
| [[MINPP1]] | +0.50 | +0.43 / +0.40 | both halves | 4e-05 |  |
| [[EID1]] | +0.49 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[TMEM9B]] | +0.48 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[NORAD]] | +0.47 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[CLIC1]] | +0.47 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[BBS10]] | +0.47 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[GJB2]] | +0.47 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[MALL]] | +0.47 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[ARPC5]] | +0.46 | +0.42 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA6L9]] | -0.52 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[GUCA1B]] | -0.50 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[PPP2R2D]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[TIMM44]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MAP2K2]] | -0.49 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[TMEM91]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TMEM258]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ATP5MC2]] | -0.48 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[COG7]] | -0.47 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[EEF1D]] | -0.47 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[LRSAM1]] | -0.47 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[TAF15]] | -0.45 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB5]] | B | SERPINB5 activity raises GALNT4's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 1.76× lower at baseline in the lines without SERPINB5 | 0.051 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[ACSL5]] | B | ACSL5 activity raises GALNT4's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without ACSL5 | 0.063 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.295). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.7, 19.7); signed map (-6.9, 37.9). **Vector** length 95.4, 20.9% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.9 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +3.9 | +1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +2.8 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.9 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -0.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.33 — chr12:89,519,412-89,524,796 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GalNAc-T4 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4A0](https://www.uniprot.org/uniprotkb/Q8N4A0) (Polypeptide N-acetylgalactosaminyltransferase 4):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor. Has a highest activity toward Muc7, EA2 and Muc2, with a lowest activity than GALNT2. Glycosylates 'Thr-57' of SELPLG.

**Summary**, from NCBI Gene [8693](https://www.ncbi.nlm.nih.gov/gene/8693):

> This gene encodes a member of the UDP-N-acetyl-alpha-D-galactosamine:polypeptide N-acetylgalactosaminyltransferase (GalNAc-T) family of enzymes. GalNAc-Ts initiate mucin-type O-linked glycosylation in the Golgi apparatus by catalyzing the transfer of GalNAc to serine and threonine residues on target proteins. They are characterized by an N-terminal transmembrane domain, a stem region, a lumenal catalytic domain containing a GT1 motif and Gal/GalNAc transferase motif, and a C-terminal …

**Accessions** — [HGNC:4126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4126) · Entrez [8693](https://www.ncbi.nlm.nih.gov/gene/8693) · UniProt [Q8N4A0](https://www.uniprot.org/uniprotkb/Q8N4A0) · Ensembl [ENSG00000257594](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257594)

## Data

Gene col 15052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15052); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15052]; `tensor/DDL_lfc|DDL_z.npy` [15052]; `embed/gene_vectors.npy` [15052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15052 or target_col == 15052). Every well: [[GALNT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
