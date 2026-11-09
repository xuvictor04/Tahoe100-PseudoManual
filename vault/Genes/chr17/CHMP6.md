---
symbol: "CHMP6"
type: "gene"
col: 10684
ensembl_id: "ENSG00000176108"
name: "charged multivesicular body protein 6"
location: "17q25.3"
module: 1
arm: "+"
pooled_cpm: 12.94
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CHMP6

*charged multivesicular body protein 6* — 17q25.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.484× (z -14.9, q 0e+00, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMF1]] (+0.65, fdr 1e-05), [[ZNF839]] (+0.61, fdr 2e-05), [[ACSF3]] (+0.61, fdr 8e-06); moves opposite to [[SAP30-DT]] (-0.62, fdr 1e-05), [[ARSK]] (-0.62, fdr 7e-06), [[POGLUT2]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10684.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +3.7 | 0.15 | 9/47 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.27× | +3.3 | 0.32 | 3/48 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.25× | +3.1 | 0.37 | 9/46 (J82, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10684.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.484×** | -14.9 | 0e+00 | 38/46 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.512×** | -9.7 | 7e-20 | 36/45 (NCI-H23, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.513×** | -9.7 | 7e-20 | 38/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.521×** | -9.4 | 5e-19 | 33/47 (KATO III, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.550×** | -8.7 | 5e-16 | 37/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.668×** | -8.3 | 1e-14 | 29/47 (HEC-1-A, RKO, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.578×** | -7.9 | 2e-13 | 27/47 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.595×** | -7.5 | 4e-12 | 27/47 (KATO III, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.712×** | -7.0 | 2e-10 | 29/47 (RPMI-7951, SW1417, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.621×** | -6.6 | 2e-09 | 26/44 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.633×** | -6.4 | 1e-08 | 23/44 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.643×** | -6.2 | 4e-08 | 20/41 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.743×** | -6.1 | 6e-08 | 21/48 (NCI-H2347, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -5.1 | 1e-05 | 17/47 (J82, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.695×** | -5.1 | 1e-05 | 19/47 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.733×** | -4.5 | 3e-04 | 13/46 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.826×** | -3.9 | 0.003 | 9/48 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.781×** | -3.4 | 0.016 | 8/44 (HepG2/C3A, HEC-1-A, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.807×** | -3.0 | 0.068 | 10/46 (A549, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **0.800×** | -3.0 | 0.068 | 12/44 (RPMI-7951, SW1417, …) | inconsistent across doses |  |
| [[Silodosin (drug)]] 5 µM |  | **0.807×** | -3.0 | 0.068 | 11/44 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.818×** | -2.9 | 0.081 | 6/45 (PANC-1, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 19.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 22.8 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0238× (z -22.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0661× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H2347 (line)]] | alt | 6.65 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.299× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0951× (z -9.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0953× (z -9.5) |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -10.4) |
| [[SW480 (line)]] | alt | 11.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -12.4) |
| [[A-172 (line)]] | wt | 13.3 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.220× (z -8.6) |
| [[C-33 A (line)]] | alt | 7.87 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0666× (z -9.3) |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0946× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -8.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[H4 (line)]] | wt | 22.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -13.0) |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0607× (z -15.4) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[KATO III (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.195× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[PANC-1 (line)]] | alt | 19.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -9.1) |
| [[RKO (line)]] | wt | 9.74 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -9.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -9.2) |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMF1]] | +0.65 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ZNF839]] | +0.61 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[ACSF3]] | +0.61 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[REXO1]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[RRP7A]] | +0.60 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ANKLE2]] | +0.60 | +0.51 / +0.67 | both halves | 1e-05 | pathway: Mitotic Anaphase |
| [[PUF60]] | +0.60 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[RTL6]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[CIAO1]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[COA7]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[JMJD4]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ZSCAN22]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAP30-DT]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ARSK]] | -0.62 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[POGLUT2]] | -0.57 | -0.46 / -0.71 | both halves | 3e-05 |  |
| [[GMCL1]] | -0.57 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PAIP2B]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[HERC3]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[FUCA1]] | -0.56 | -0.37 / -0.61 | both halves | 8e-05 |  |
| [[PRCP]] | -0.56 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[PIK3C2A]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[CRLS1]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[APAF1]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 | pathway: Programmed Cell Death |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (5.7, -16.2); signed map (1.8, -34.2). **Vector** length 64.3, 10.2% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.3 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.5 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.1 | -6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.8 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.4 | -6.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | charged multivesicular body protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:80,991,598-81,009,517 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11749, VPS20 |
| Gene groups (HGNC) | Charged multivesicular body proteins; ESCRT-III |
| Reactome | 29 pathways, smallest: Translation of Replicase and Assembly of the Replication Transcription Complex_9679504; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676; Pyroptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FZ7](https://www.uniprot.org/uniprotkb/Q96FZ7) (Charged multivesicular body protein 6):

> Probable core component of the endosomal sorting required for transport complex III (ESCRT-III) which is involved in multivesicular bodies (MVBs) formation and sorting of endosomal cargo proteins into MVBs. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling degradation of membrane proteins, such as stimulated growth factor receptors, lysosomal enzymes and lipids. The …

**Summary**, from NCBI Gene [79643](https://www.ncbi.nlm.nih.gov/gene/79643):

> This gene encodes a member of the chromatin-modifying protein/charged multivesicular body protein family. Proteins in this family are part of the ESCRT-III (endosomal sorting complex required for transport III) which degrades surface receptors, and in biosynthesis of endosomes. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:25675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25675) · Entrez [79643](https://www.ncbi.nlm.nih.gov/gene/79643) · UniProt [Q96FZ7](https://www.uniprot.org/uniprotkb/Q96FZ7) · Ensembl [ENSG00000176108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176108)

## Data

Gene col 10684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10684); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10684]; `tensor/DDL_lfc|DDL_z.npy` [10684]; `embed/gene_vectors.npy` [10684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10684 or target_col == 10684). Every well: [[CHMP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
