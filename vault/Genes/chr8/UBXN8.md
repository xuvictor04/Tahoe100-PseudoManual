---
symbol: "UBXN8"
type: "gene"
col: 2484
ensembl_id: "ENSG00000104691"
name: "UBX domain protein 8"
location: "8p12"
module: 35
arm: "+"
pooled_cpm: 5.82
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# UBXN8

*UBX domain protein 8* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.28× (z +17.5, q 0e+00, up in 24 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.69× (z +14.6, q 1e-45, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.601× (z -7.5, q 4e-11, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHSA2P]] (+0.63, fdr 4e-05), [[HSPE1-MOB4]] (+0.61, fdr 2e-05), [[UQCC1]] (+0.61, fdr 3e-05); moves opposite to [[ARL13B]] (-0.55, fdr 3e-04), [[CDKN2D]] (-0.54, fdr 2e-04), [[UACA]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2484.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.28×** | +17.5 | 0e+00 | 24/26 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.69×** | +14.6 | 1e-45 | 37/44 (SW480, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +13.1 | 1e-36 | 8/8 (PANC-1, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +13.0 | 2e-36 | 9/13 (J82, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.3 | 5e-23 | 25/42 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +8.1 | 7e-14 | 14/27 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +7.2 | 5e-11 | 20/46 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +6.4 | 1e-08 | 16/42 (NCI-H2347, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.20×** | +6.1 | 7e-08 | 7/18 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.65×** | +5.3 | 8e-06 | 7/44 (NCI-H2347, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +5.2 | 8e-06 | 17/44 (A498, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +5.2 | 8e-06 | 14/45 (NCI-H2347, NCI-H2030, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.8 | 7e-05 | 3/12 (NCI-H2347, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.5 | 2e-04 | 12/46 (A-172, HOP62, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.4 | 3e-04 | 8/40 (NCI-H2347, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2484.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.601×** | -7.5 | 4e-11 | 23/46 (A498, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.613×** | -7.2 | 1e-10 | 23/46 (A498, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.628×** | -6.9 | 1e-09 | 20/46 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.668×** | -5.9 | 4e-07 | 15/46 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.734×** | -4.6 | 6e-04 | 12/40 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -4.5 | 7e-04 | 8/47 (A549, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.637×** | -3.5 | 0.041 | 4/45 (SHP-77, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Penfluridol (drug)]] 0.5 µM |  | 0.811× | -3.1 | 0.14 | 4/46 (HEC-1-A, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2484. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.88 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.125× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0819× (z -8.7) |
| [[KATO III (line)]] | alt | 3.85 | 0 | 1 | — | [[Entrectinib (drug)]] 5 µM 0.0770× (z -9.4) |
| [[LoVo (line)]] | wt | 4.62 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.148× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 2.78 | 0 | 1 | — | [[Delamanid (drug)]] 0.05 µM 0.0552× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 9.42 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.104× (z -9.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 14.2 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.198× (z -8.5) |
| [[A-427 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2484), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA2P]] | +0.63 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[HSPE1-MOB4]] | +0.61 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[UQCC1]] | +0.61 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[C2orf49-DT]] | +0.60 | +0.23 / +0.58 | both halves | 5e-04 |  |
| [[TYW3]] | +0.60 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[SUMO2P17]] | +0.59 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[ANKAR]] | +0.58 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[PRR3]] | +0.58 | +0.51 / +0.30 | both halves | 2e-04 |  |
| [[PEX6]] | +0.58 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[C2orf88]] | +0.58 | +0.27 / +0.42 | both halves | 3e-04 |  |
| [[WDR81]] | +0.57 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[POU6F1]] | +0.57 | +0.30 / +0.46 | both halves | 2e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL13B]] | -0.55 | -0.29 / -0.50 | both halves | 3e-04 |  |
| [[CDKN2D]] | -0.54 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[UACA]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[DOP1A]] | -0.51 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[INIP]] | -0.50 | -0.33 / -0.29 | both halves | 2e-04 |  |
| [[DHTKD1]] | -0.50 | -0.26 / -0.30 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises UBXN8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-6.3, 26.6); signed map (33.7, -17.3). **Vector** length 55.0, 7.08% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +14.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +13.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +5.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.4 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.8 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.7 | -7.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -3.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | UBX domain protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:30,729,131-30,767,006 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D8S2298E, REP8; previously UBXD6 |
| Gene groups (HGNC) | UBX domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O00124](https://www.uniprot.org/uniprotkb/O00124) (UBX domain-containing protein 8):

> Involved in endoplasmic reticulum-associated degradation (ERAD) for misfolded lumenal proteins, possibly by tethering VCP to the endoplasmic reticulum membrane. May play a role in reproduction.

**Summary**, from NCBI Gene [7993](https://www.ncbi.nlm.nih.gov/gene/7993):

> p97 or VCP (valosin-containing protein) is a versatile ATPase complex, and many cofactors are required for the p97 functional diversity. This gene encodes one of the p97 cofactors. This cofactor is a transmembrane protein and localized in the endoplasmic reticulum (ER) membrane. It tethers p97 to the ER membrane via its UBX domain. The association of this cofactor with p97 facilitates efficient ER-associated degradation of misfolded proteins. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:30307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30307) · Entrez [7993](https://www.ncbi.nlm.nih.gov/gene/7993) · UniProt [O00124](https://www.uniprot.org/uniprotkb/O00124) · Ensembl [ENSG00000104691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104691)

## Data

Gene col 2484: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2484); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2484, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2484]; `tensor/DDL_lfc|DDL_z.npy` [2484]; `embed/gene_vectors.npy` [2484]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2484 or target_col == 2484). Every well: [[UBXN8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBXN8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
