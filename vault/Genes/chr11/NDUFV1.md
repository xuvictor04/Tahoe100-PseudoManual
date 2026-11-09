---
symbol: "NDUFV1"
type: "gene"
col: 9543
ensembl_id: "ENSG00000167792"
name: "NADH:ubiquinone oxidoreductase core subunit V1"
location: "11q13.2"
module: 57
arm: "+"
pooled_cpm: 48.12
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# NDUFV1

*NADH:ubiquinone oxidoreductase core subunit V1* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.93× (z +14.7, q 0e+00, up in 46 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.43× (z +3.5, q 0.023, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.628× (z -8.9, q 2e-16, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6AP2]] (+0.67, fdr 1e-05), [[AKR7A2]] (+0.65, fdr 1e-05), [[NDUFS2]] (+0.64, fdr 1e-05); moves opposite to [[LINC01033]] (-0.60, fdr 2e-05), [[SPEN]] (-0.59, fdr 1e-05), [[LINC02516]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.93×** | +14.7 | 0e+00 | 46/46 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.38×** | +11.4 | 2e-27 | 39/41 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.97×** | +9.2 | 4e-18 | 47/48 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.87×** | +8.6 | 2e-15 | 45/48 (SW480, Panc 03.27, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +8.3 | 1e-14 | 41/47 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.10×** | +7.9 | 3e-13 | 37/42 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.59×** | +6.4 | 2e-08 | 38/48 (SW480, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.49×** | +5.2 | 1e-05 | 30/48 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.41×** | +4.5 | 4e-04 | 28/48 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.23×** | +4.0 | 0.004 | 24/48 (NCI-H2030, Panc 03.27, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.023 | 23/47 (AsPC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.055 | 22/48 (NCI-H2347, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.069 | 19/48 (LoVo, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.093 | 23/48 (NCI-H1792, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9543.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.628×** | -8.9 | 2e-16 | 39/48 (HS-578T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.677×** | -5.3 | 3e-05 | 30/47 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.711×** | -4.6 | 7e-04 | 31/48 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -3.6 | 0.042 | 25/48 (A498, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.782× | -3.3 | 0.10 | 19/48 (A498, H4, …) | rises with dose |  |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.793× | -3.0 | 0.24 | 19/48 (hTERT-HPNE, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 68.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -11.5) |
| [[LoVo (line)]] | wt | 33.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 37.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -11.1) |
| [[SW480 (line)]] | alt | 54.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 41.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 45.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 60.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 119 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 28.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 57.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -10.7) |
| [[A-172 (line)]] | wt | 32.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 61.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -10.9) |
| [[A549 (line)]] | wt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 45.8 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.137× (z -9.5) |
| [[C-33 A (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C32 (line)]] | wt | 39.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HCT15 (line)]] | alt | 46.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 61.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 40.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -13.0) |
| [[LS 180 (line)]] | wt | 50.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 58.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +11.6) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H661 (line)]] | alt | 53.3 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0762× (z -10.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 86.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -8.6) |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.1) |
| [[A498 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6AP2]] | +0.67 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[AKR7A2]] | +0.65 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[NDUFS2]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[UNC45A]] | +0.60 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[WDR5]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ANAPC5]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[RPA1]] | +0.59 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[CLPTM1]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SHQ1]] | +0.58 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[FLYWCH2]] | +0.58 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TMEM219]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[DHPS]] | +0.58 | +0.58 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01033]] | -0.60 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[SPEN]] | -0.59 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[LINC02516]] | -0.58 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[KCNMB3]] | -0.57 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[NANOS3]] | -0.57 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ACVR1C]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ADNP2]] | -0.56 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[CAVIN4]] | -0.56 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[OXTR]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[LINC00486]] | -0.54 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ARAP2]] | -0.54 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[SMCO2]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NDUFV1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.3, -12.8); signed map (-38.1, -11.6). **Vector** length 94.9, 26.2% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.6 | +9.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.4 | +8.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.4 | +2.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.3 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.9 | +6.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | +1.8 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.4 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.1 | -8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.9 | -3.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.5 | -1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Mozavaptan (drug)]] 0.05 µM |  | -2.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase core subunit V1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,605,653-67,612,554 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CI-51K |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits; Flavoproteins |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Complex I biogenesis; Mitochondrial protein degradation; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P49821](https://www.uniprot.org/uniprotkb/P49821) (NADH dehydrogenase):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor. Part of the peripheral arm of the enzyme, where the electrons from NADH are accepted by flavin mononucleotide (FMN) and then passed along a chain of iron-sulfur clusters by electron tunnelling to the final acceptor ubiquinone. Contains FMN, which is the initial electron acceptor as well as …

**Summary**, from NCBI Gene [4723](https://www.ncbi.nlm.nih.gov/gene/4723):

> The mitochondrial respiratory chain provides energy to cells via oxidative phosphorylation and consists of four membrane-bound electron-transporting protein complexes (I-IV) and an ATP synthase (complex V). This gene encodes a 51 kDa subunit of the NADH:ubiquinone oxidoreductase complex I; a large complex with at least 45 nuclear and mitochondrial encoded subunits that liberates electrons from NADH and channels them to ubiquinone. This subunit carries the NADH-binding site as well as flavin …

**Accessions** — [HGNC:7716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7716) · Entrez [4723](https://www.ncbi.nlm.nih.gov/gene/4723) · UniProt [P49821](https://www.uniprot.org/uniprotkb/P49821) · Ensembl [ENSG00000167792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167792)

## Data

Gene col 9543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9543); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9543]; `tensor/DDL_lfc|DDL_z.npy` [9543]; `embed/gene_vectors.npy` [9543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9543 or target_col == 9543). Every well: [[NDUFV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
