---
symbol: "KLHL2"
type: "gene"
col: 3053
ensembl_id: "ENSG00000109466"
name: "kelch like family member 2"
location: "4q32.3"
module: 4
arm: "+"
pooled_cpm: 37.52
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# KLHL2

*kelch like family member 2* — 4q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.29× (z +4.5, q 0.003, up in 21 of 48 measured lines) ⚠ unreliable plate only.
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.567× (z -14.5, q 1e-44, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PROSER1]] (+0.59, fdr 1e-05), [[AGPS]] (+0.57, fdr 1e-05), [[USP46]] (+0.57, fdr 1e-05); moves opposite to [[ZKSCAN1]] (-0.58, fdr 1e-05), [[TOX4]] (-0.54, fdr 1e-05), [[RSPRY1]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.5 | 0.003 | 21/48 (A498, A-427, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.20× | +3.3 | 0.27 | 10/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.19× | +3.1 | 0.38 | 11/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3053.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -14.5 | 1e-44 | 38/47 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.525×** | -11.6 | 9e-29 | 37/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.556×** | -10.6 | 6e-24 | 35/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.677×** | -10.0 | 2e-21 | 27/47 (HS-578T, NCI-H23, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.647×** | -7.9 | 5e-13 | 33/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.732×** | -5.6 | 2e-06 | 25/47 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.750×** | -5.2 | 2e-05 | 24/48 (RKO, HS-578T, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.743×** | -5.2 | 2e-05 | 20/37 (NCI-H2030, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -5.2 | 2e-05 | 24/48 (HT-29, BT-474, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.756×** | -5.1 | 2e-05 | 25/47 (HCT15, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.758×** | -4.8 | 7e-05 | 23/48 (PANC-1, BT-474, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.777×** | -4.6 | 3e-04 | 25/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **0.804×** | -3.9 | 0.003 | 22/45 (SW480, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.798×** | -3.8 | 0.007 | 20/42 (SW48, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.819×** | -3.6 | 0.012 | 18/47 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.826×** | -3.5 | 0.020 | 17/47 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 58.9 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -12.8) |
| [[SW480 (line)]] | alt | 46.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -20.0) |
| [[SHP-77 (line)]] | alt | 116 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -11.9) |
| [[BT-474 (line)]] | alt | 33.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.205× (z -9.4) |
| [[KATO III (line)]] | alt | 31.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -11.2) |
| [[A-172 (line)]] | wt | 25.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -10.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A549 (line)]] | wt | 31.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 32.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 97.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H1792 (line)]] | alt | 45.0 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0594× (z -13.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 43.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[PANC-1 (line)]] | alt | 35.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW48 (line)]] | wt | 43.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[A-427 (line)]] | wt | 33.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.470× (z -9.8) |
| [[A498 (line)]] | wt | 49.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -11.4) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HCT15 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0715× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[HOP62 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.191× (z -13.1) ⚠ transcription drop; cell-cycle shift, explains ~89% of this change |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -15.3) ⚠ cell-cycle shift, explains ~54% of this change |
| [[hTERT-HPNE (line)]] | wt | 29.7 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0629× (z -8.8) ⚠ toxic |
| [[J82 (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[LoVo (line)]] | wt | 37.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.420× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 45.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 33.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.351× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[Panc 03.27 (line)]] | alt | 34.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -8.9) |
| [[RKO (line)]] | wt | 47.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -9.5) |
| [[SNU-1 (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[SW 900 (line)]] | alt | 39.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -10.7) |
| [[SW1417 (line)]] | alt | 33.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.7) |
| [[AN3 CA (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PROSER1]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[AGPS]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[USP46]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[VWA8]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MTMR8]] | +0.56 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[SNX7]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[GSR]] | +0.56 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[UBE2E3]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[KPNA3]] | +0.55 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[HEATR3]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[KPNA1]] | +0.54 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[SLC22A15]] | +0.54 | +0.62 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN1]] | -0.58 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[TOX4]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[RSPRY1]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[HMGCL]] | -0.54 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[RARA]] | -0.50 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[FNIP1]] | -0.50 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[RNMT]] | -0.49 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[KDM5B]] | -0.48 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[SYNRG]] | -0.48 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[RASA4B]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[BET1]] | -0.48 | -0.44 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KLHL2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.494). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.5, -34.0); signed map (-15.6, -46.9). **Vector** length 89.4, 19.6% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -14.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -2.9 | -5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | -2.7 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -2.3 | -10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -5.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.3 — chr4:165,207,561-165,323,156 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAV |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95198](https://www.uniprot.org/uniprotkb/O95198) (Kelch-like protein 2):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex that mediates the ubiquitination of target proteins, such as NPTXR, WNK1, WNK3 and WNK4, leading most often to their proteasomal degradation. The BCR(KLHL2) complex catalyzes ubiquitination and degradation of NPTXR (By similarity). Responsible for degradative ubiquitination of the WNK kinases WNK1, WNK3 and WNK4. Plays a role in the reorganization of the actin cytoskeleton. Promotes growth of cell projections in …

**Summary**, from NCBI Gene [11275](https://www.ncbi.nlm.nih.gov/gene/11275):

> Enables actin binding activity; identical protein binding activity; and ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process and protein ubiquitination. Located in actin cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6353](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6353) · Entrez [11275](https://www.ncbi.nlm.nih.gov/gene/11275) · UniProt [O95198](https://www.uniprot.org/uniprotkb/O95198) · Ensembl [ENSG00000109466](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109466)

## Data

Gene col 3053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3053); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3053]; `tensor/DDL_lfc|DDL_z.npy` [3053]; `embed/gene_vectors.npy` [3053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3053 or target_col == 3053). Every well: [[KLHL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
