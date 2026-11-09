---
symbol: "PRKACB"
type: "gene"
col: 6662
ensembl_id: "ENSG00000142875"
name: "protein kinase cAMP-activated catalytic subunit beta"
location: "1p31.1"
module: 117
arm: "+"
pooled_cpm: 79.93
n_lines_expressing: 42
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# PRKACB

*protein kinase cAMP-activated catalytic subunit beta* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.38× (z +4.8, q 9e-04, up in 24 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.588× (z -11.2, q 2e-26, down in 31 of 40 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.267× (z -10.3, q 1e-22, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR135]] (+0.58, fdr 1e-05), [[TDO2]] (+0.57, fdr 3e-05), [[VEGFD]] (+0.54, fdr 2e-05); moves opposite to [[ARHGAP45]] (-0.53, fdr 4e-05), [[CLMN]] (-0.53, fdr 4e-05), [[DENND3]] (-0.52, fdr 1e-04).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PKP2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC01355]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.8 | 9e-04 | 24/40 (LoVo, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +4.3 | 0.005 | 19/40 (AsPC-1, C32, …) | top dose only | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.28× | +3.4 | 0.11 | 19/39 (SW480, C32, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.11 | 15/40 (SW480, LoVo, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | 1.52× | +3.3 | 0.11 | 17/41 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.24× | +3.3 | 0.11 | 16/40 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.24× | +3.2 | 0.11 | 17/40 (SW480, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.14 | 12/40 (NCI-H2030, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6662.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.588×** | -11.2 | 2e-26 | 31/40 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.480×** | -11.0 | 2e-25 | 36/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.267×** | -10.3 | 1e-22 | 40/41 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.534×** | -9.4 | 1e-18 | 33/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.559×** | -8.7 | 4e-16 | 32/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.562×** | -8.6 | 7e-16 | 31/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.642×** | -6.4 | 2e-08 | 25/40 (A498, PANC-1, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.467×** | -6.0 | 2e-07 | 26/40 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.692×** | -5.3 | 8e-06 | 26/39 (NCI-H460, AN3 CA, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.681×** | -5.1 | 2e-05 | 25/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **0.722×** | -4.9 | 6e-05 | 27/40 (SW 900, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.828×** | -4.0 | 0.003 | 19/41 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.763×** | -3.9 | 0.005 | 24/40 (NCI-H460, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.775×** | -3.8 | 0.006 | 17/40 (Panc 03.27, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.784×** | -3.3 | 0.039 | 16/40 (NCI-H2030, AsPC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.800×** | -3.0 | 0.089 | 13/39 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.799×** | -3.0 | 0.096 | 17/40 (SW 1271, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 209 | 0 | 9 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -19.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.209× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 168 | 0 | 8 (8 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.225× (z -14.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 112 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -15.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.147× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 78.5 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 111 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -21.9) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.257× (z -8.6) |
| [[LoVo (line)]] | wt | 88.0 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.422× (z -9.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.209× (z -8.8) |
| [[SW480 (line)]] | alt | 125 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -12.7) ⚠ cell-cycle shift, explains ~76% of this change |
| [[A549 (line)]] | wt | 57.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[AN3 CA (line)]] | alt | 166 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0646× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[HOP62 (line)]] | alt | 66.6 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.122× (z -10.7) |
| [[J82 (line)]] | alt | 76.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.366× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 167 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 67.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -14.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-427 (line)]] | wt | 58.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.372× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[HS-578T (line)]] | alt | 99.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -10.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H1573 (line)]] | alt | 41.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[RPMI-7951 (line)]] | alt | 104 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.172× (z -9.1) |
| [[SNU-423 (line)]] | alt | 81.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -14.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SW 1088 (line)]] | alt | 121 | 0 | 2 (2 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.110× (z -9.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 83.6 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.320× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~63% of this change |
| [[BT-474 (line)]] | alt | 49.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.288× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 69.0 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0816× (z -8.9) |
| [[Hs 766T (line)]] | wt | 78.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.394× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.275× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 91.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.379× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 116 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR135]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[TDO2]] | +0.57 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[VEGFD]] | +0.54 | +0.47 / +0.56 | both halves | 2e-05 | pathway: Signaling by VEGF |
| [[L3HYPDH]] | +0.52 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[FTX]] | +0.51 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[ZNF804A]] | +0.50 | +0.44 / +0.37 | both halves | 9e-05 |  |
| [[MPDZ]] | +0.50 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[STXBP4]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ABCC2]] | +0.49 | +0.38 / +0.42 | both halves | 7e-05 |  |
| [[GPATCH2]] | +0.48 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[BAG2]] | +0.48 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[AP5M1]] | +0.48 | +0.50 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP45]] | -0.53 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[CLMN]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[DENND3]] | -0.52 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[KLHL26]] | -0.48 | -0.37 / -0.24 | both halves | 4e-04 |  |
| [[TCN2]] | -0.47 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[GPRC5A]] | -0.47 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[RALGDS]] | -0.46 | -0.49 / -0.32 | both halves | 2e-04 | pathway: MAPK family signaling cascades |
| [[FOXO6]] | -0.46 | -0.37 / -0.23 | both halves | 5e-04 | pathway: Intracellular signaling by second messengers |
| [[DNAAF3]] | -0.46 | -0.46 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[RDH13]] | -0.46 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[HS3ST3B1]] | -0.46 | -0.39 / -0.35 | both halves | 1e-04 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[SERPINB1]] | -0.45 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[TNIP2]] | -0.45 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKP2]] | B | PKP2 activity lowers PRKACB's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.27× higher at baseline in the lines without PKP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[HS3ST3B1]] | B | HS3ST3B1 activity raises PRKACB's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 2.11× lower at baseline in the lines without HS3ST3B1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[ZNF804A]] | B | ZNF804A activity raises PRKACB's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without ZNF804A | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01355]] | B | PRKACB activity raises LINC01355's level | lines that do not express PRKACB (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without PRKACB | 0.091 | ⚠ within organs, on part of the lines; also absent: FADS1, ZNF134, IPCEF1 |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.473). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-5.3, 50.2); signed map (51.2, -13.2). **Vector** length 74.9, 17.6% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.3 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.9 | +2.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.4 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.1 | -11.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -6.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase cAMP-activated catalytic subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:84,078,062-84,238,498 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKACb |
| Gene groups (HGNC) | Protein kinase A subunits; Protein kinase A family; Centriolar satellite proteins |
| Reactome | 73 pathways, smallest: PKA-mediated phosphorylation of key metabolic factors; HDL assembly; ROBO receptors bind AKAP5 |
| Matched by | ensembl_id |

**Function**, from UniProt [P22694](https://www.uniprot.org/uniprotkb/P22694) (cAMP-dependent protein kinase catalytic subunit beta):

> Mediates cAMP-dependent signaling triggered by receptor binding to GPCRs. PKA activation regulates diverse cellular processes such as cell proliferation, the cell cycle, differentiation and regulation of microtubule dynamics, chromatin condensation and decondensation, nuclear envelope disassembly and reassembly, as well as regulation of intracellular transport mechanisms and ion flux. Regulates the abundance of compartmentalized pools of its regulatory subunits through phosphorylation of PJA2 …

**Summary**, from NCBI Gene [5567](https://www.ncbi.nlm.nih.gov/gene/5567):

> The protein encoded by this gene is a member of the serine/threonine protein kinase family. The encoded protein is a catalytic subunit of cAMP (cyclic AMP)-dependent protein kinase, which mediates signalling though cAMP. cAMP signaling is important to a number of processes, including cell proliferaton and differentiation. Multiple alternatively spliced transcript variants encoding distinct isoforms have been observed. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:9381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9381) · Entrez [5567](https://www.ncbi.nlm.nih.gov/gene/5567) · UniProt [P22694](https://www.uniprot.org/uniprotkb/P22694) · Ensembl [ENSG00000142875](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142875)

## Data

Gene col 6662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6662); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6662]; `tensor/DDL_lfc|DDL_z.npy` [6662]; `embed/gene_vectors.npy` [6662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6662 or target_col == 6662). Every well: [[PRKACB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKACB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
