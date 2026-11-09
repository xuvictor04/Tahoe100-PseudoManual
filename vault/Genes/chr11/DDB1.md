---
symbol: "DDB1"
type: "gene"
col: 9571
ensembl_id: "ENSG00000167986"
name: "damage specific DNA binding protein 1"
location: "11q12.2"
module: 42
arm: "+"
pooled_cpm: 133.29
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# DDB1

*damage specific DNA binding protein 1* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 2.87× (z +10.6, q 1e-23, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.807× (z -5.6, q 1e-05, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPA]] (+0.77, fdr 7e-06), [[SEC61A1]] (+0.76, fdr 7e-06), [[SAR1A]] (+0.76, fdr 7e-06); moves opposite to [[CMTR2]] (-0.65, fdr 7e-06), [[DDX52]] (-0.63, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.87×** | +10.6 | 1e-23 | 45/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.22×** | +8.0 | 2e-13 | 46/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +6.9 | 1e-09 | 35/48 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +6.6 | 7e-09 | 39/48 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.18× | +4.3 | 0.002 | 20/49 (C32, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.23×** | +4.0 | 0.006 | 24/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.23×** | +3.9 | 0.007 | 22/44 (SK-MEL-2, A549, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.20×** | +3.6 | 0.025 | 23/49 (SW480, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.5 | 0.030 | 20/38 (SNU-423, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.032 | 22/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.4 | 0.040 | 22/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.051 | 12/48 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.073 | 19/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.073 | 8/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.073 | 18/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.082 | 14/48 (H4, LoVo, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.12× | +3.0 | 0.096 | 3/49 (SW 900, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9571.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.807×** | -5.6 | 1e-05 | 29/48 (J82, SW 900, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.747×** | -5.4 | 2e-05 | 32/48 (J82, SNU-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.765×** | -5.2 | 5e-05 | 29/48 (SW 900, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.789×** | -4.4 | 0.002 | 27/48 (J82, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.809×** | -4.1 | 0.005 | 25/48 (J82, H4, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.811×** | -3.9 | 0.009 | 24/47 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.830×** | -3.6 | 0.027 | 23/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.827×** | -3.5 | 0.027 | 25/47 (LoVo, C-33 A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.833×** | -3.5 | 0.027 | 23/48 (AsPC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.825×** | -3.4 | 0.034 | 23/47 (HS-578T, H4, …) | all doses, flat | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.842× | -3.3 | 0.043 | 18/49 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.3 | 0.043 | 19/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.847× | -3.2 | 0.062 | 19/49 (CFPAC-1, NCI-H2122, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 165 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 117 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +14.7) | — |
| [[AsPC-1 (line)]] | alt | 175 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.453× (z -9.7) |
| [[J82 (line)]] | alt | 169 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.424× (z -12.8) |
| [[LoVo (line)]] | wt | 144 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +11.7) | — |
| [[A549 (line)]] | wt | 123 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 83.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 157 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.04× (z +9.2) | — |
| [[A-172 (line)]] | wt | 86.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.476× (z -8.9) |
| [[A-427 (line)]] | wt | 155 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 187 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.526× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 123 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 114 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 142 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.04× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 97.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[RKO (line)]] | wt | 134 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.41× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 67.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 155 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 120 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 98.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 169 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 94.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 145 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 168 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 138 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 100.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPA]] | +0.77 | +0.79 / +0.73 | both halves | 7e-06 | STRING 469 |
| [[SEC61A1]] | +0.76 | +0.76 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR |
| [[SAR1A]] | +0.76 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[SEC13]] | +0.73 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.72 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.72 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[NUS1]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.72 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[MSTO2P]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[PDXDC2P]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[CALU]] | +0.71 | +0.72 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMTR2]] | -0.65 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[DDX52]] | -0.63 | -0.63 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, -31.0); signed map (-52.5, 6.6). **Vector** length 117, 37.1% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.58 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.55 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.55 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +6.4 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.7 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +4.6 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +10.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.2 | +1.8 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +1.9 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -9.1 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.0 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.5 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | damage specific DNA binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,299,451-61,342,596 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Nucleotide excision repair |
| Hallmark sets | DNA_REPAIR |
| Reactome | 16 pathways, smallest: Recognition of DNA damage by PCNA-containing replication complex; DNA Damage Recognition in GG-NER; Dual Incision in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16531](https://www.uniprot.org/uniprotkb/Q16531) (DNA damage-binding protein 1):

> Involved in DNA repair and protein ubiquitination, as part of the UV-DDB complex and DCX (DDB1-CUL4-X-box) complexes, respectively. Core component of the UV-DDB complex (UV-damaged DNA-binding protein complex), a complex that recognizes UV-induced DNA damage and recruits proteins of the nucleotide excision repair pathway (the NER pathway) to initiate DNA repair. The UV-DDB complex preferentially binds to cyclobutane pyrimidine dimers (CPD), 6-4 photoproducts (6-4 PP), apurinic sites and short …

**Summary**, from NCBI Gene [1642](https://www.ncbi.nlm.nih.gov/gene/1642):

> The protein encoded by this gene is the large subunit (p127) of the heterodimeric DNA damage-binding (DDB) complex while another protein (p48) forms the small subunit. This protein complex functions in nucleotide-excision repair and binds to DNA following UV damage. Defective activity of this complex causes the repair defect in patients with xeroderma pigmentosum complementation group E (XPE) - an autosomal recessive disorder characterized by photosensitivity and early onset of carcinomas. …

**Accessions** — [HGNC:2717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2717) · Entrez [1642](https://www.ncbi.nlm.nih.gov/gene/1642) · UniProt [Q16531](https://www.uniprot.org/uniprotkb/Q16531) · Ensembl [ENSG00000167986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167986)

## Data

Gene col 9571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9571); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9571]; `tensor/DDL_lfc|DDL_z.npy` [9571]; `embed/gene_vectors.npy` [9571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9571 or target_col == 9571). Every well: [[DDB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
