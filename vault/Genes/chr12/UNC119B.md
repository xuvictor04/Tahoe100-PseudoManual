---
symbol: "UNC119B"
type: "gene"
col: 10668
ensembl_id: "ENSG00000175970"
name: "unc-119 lipid binding chaperone B"
location: "12q24.31"
module: 46
arm: "+"
pooled_cpm: 12.87
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# UNC119B

*unc-119 lipid binding chaperone B* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +10.6, q 2e-23, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.436× (z -6.5, q 6e-08, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF2D]] (+0.61, fdr 1e-05), [[USP21]] (+0.60, fdr 1e-05), [[FBXW4]] (+0.58, fdr 6e-05); moves opposite to [[RAB10]] (-0.52, fdr 3e-05), [[ACSL3]] (-0.49, fdr 1e-04), [[ATP2B4]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10668.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +10.6 | 2e-23 | 36/45 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +10.0 | 3e-21 | 30/47 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +7.7 | 2e-12 | 24/47 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +7.1 | 1e-10 | 27/41 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.4 | 8e-06 | 23/48 (HT-29, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.8 | 2e-04 | 20/44 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +4.7 | 2e-04 | 18/40 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 3e-04 | 14/47 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +3.9 | 0.007 | 17/46 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.009 | 17/46 (hTERT-HPNE, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.009 | 13/46 (SK-MEL-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.019 | 12/48 (A549, A-427, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.4 | 0.025 | 10/21 (hTERT-HPNE, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.069 | 13/47 (BT-474, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.069 | 7/46 (HOP62, NCI-H1792, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10668.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.436×** | -6.5 | 6e-08 | 26/48 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -6.0 | 5e-07 | 25/48 (MIA PaCa-2, A498, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -4.9 | 1e-04 | 20/41 (SK-MEL-2, SHP-77, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.554×** | -4.6 | 6e-04 | 16/43 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.762×** | -4.0 | 0.006 | 8/48 (C-33 A, LS 180, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.781×** | -3.5 | 0.038 | 17/46 (A549, RKO, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | **0.795×** | -3.3 | 0.082 | 5/47 (HEC-1-A, SW 900, …) | top dose only | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.863× | -3.1 | 0.14 | 11/48 (SHP-77, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Furosemide (drug)]] 5 µM |  | 0.865× | -3.0 | 0.15 | 5/48 (SK-MEL-2, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 11.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +9.3) | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.156× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0953× (z -10.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2D]] | +0.61 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[USP21]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[FBXW4]] | +0.58 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[LINC00938]] | +0.58 | +0.37 / +0.51 | both halves | 9e-05 |  |
| [[KLHL11]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[GSK3A]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[HLA-H]] | +0.54 | +0.45 / +0.37 | both halves | 8e-05 |  |
| [[TMED8]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[C14orf28]] | +0.54 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[DDX59]] | +0.54 | +0.39 / +0.42 | both halves | 6e-05 |  |
| [[FBRS]] | +0.54 | +0.44 / +0.34 | both halves | 1e-04 |  |
| [[C5orf15]] | +0.53 | +0.32 / +0.42 | both halves | 2e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB10]] | -0.52 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ACSL3]] | -0.49 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[ATP2B4]] | -0.47 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[RSU1]] | -0.47 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[CBR1]] | -0.46 | -0.38 / -0.23 | both halves | 5e-04 |  |
| [[GIPC1]] | -0.46 | -0.28 / -0.32 | both halves | 3e-04 |  |
| [[TTC3P1]] | -0.45 | -0.32 / -0.27 | both halves | 3e-04 |  |
| [[RABGAP1L]] | -0.45 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[TECPR1]] | -0.45 | -0.34 / -0.19 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UNC119B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.444). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-14.1, -22.8); signed map (24.0, -21.7). **Vector** length 73.9, 12.2% of its response variance represented; |z| ≥ 3 in 908 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +10.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +7.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.2 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.7 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +10.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.5 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +2.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.2 | -6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.4 | -4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.7 | -2.6 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | unc-119 lipid binding chaperone B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,710,458-120,723,640 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5139, POC7B |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: Trafficking of myristoylated proteins to the cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NIH7](https://www.uniprot.org/uniprotkb/A6NIH7) (Protein unc-119 homolog B):

> Myristoyl-binding protein that acts as a cargo adapter: specifically binds the myristoyl moiety of a subset of N-terminally myristoylated proteins and is required for their localization. Binds myristoylated NPHP3 and plays a key role in localization of NPHP3 to the primary cilium membrane. Does not bind all myristoylated proteins. Probably plays a role in trafficking proteins in photoreceptor cells.

**Summary**, from NCBI Gene [84747](https://www.ncbi.nlm.nih.gov/gene/84747):

> Enables lipid binding activity. Involved in cilium assembly and lipoprotein transport. Located in ciliary transition zone and sperm flagellum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16488) · Entrez [84747](https://www.ncbi.nlm.nih.gov/gene/84747) · UniProt [A6NIH7](https://www.uniprot.org/uniprotkb/A6NIH7) · Ensembl [ENSG00000175970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175970)

## Data

Gene col 10668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10668); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10668]; `tensor/DDL_lfc|DDL_z.npy` [10668]; `embed/gene_vectors.npy` [10668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10668 or target_col == 10668). Every well: [[UNC119B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC119B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
