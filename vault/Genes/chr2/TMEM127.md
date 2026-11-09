---
symbol: "TMEM127"
type: "gene"
col: 5789
ensembl_id: "ENSG00000135956"
name: "transmembrane protein 127"
location: "2q11.2"
module: 7
arm: "+"
pooled_cpm: 23.26
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TMEM127

*transmembrane protein 127* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.72× (z +9.2, q 2e-17, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.611× (z -11.8, q 2e-29, down in 38 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 0.763× (z -4.4, q 9e-04, down in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.264×, KATO III 0.254×, SW480 0.439×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1792 0.0592×, hTERT-HPNE 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LOX-IMVI 0.125×, C32 0.185×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Silodosin (drug)]] 5 µM in 1 line (C-33 A 0.0828×); [[Naproxen (drug)]] 0.05 µM in 1 line (SW48 0.0843×); [[Harringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.0923×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM115]] (+0.60, fdr 1e-05), [[SPRING1]] (+0.60, fdr 1e-05), [[RAB5C]] (+0.60, fdr 1e-05); moves opposite to [[PTBP2]] (-0.50, fdr 2e-04), [[ANKRD26]] (-0.50, fdr 2e-05), [[LINC01473]] (-0.49, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +9.2 | 2e-17 | 37/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +8.3 | 3e-14 | 35/48 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +8.1 | 7e-14 | 37/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.8 | 1e-06 | 30/48 (RKO, A-172, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +5.2 | 2e-05 | 26/48 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.22×** | +4.8 | 2e-04 | 25/47 (NCI-H460, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.049 | 10/48 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.22× | +3.2 | 0.11 | 13/47 (A498, NCI-H460, …) | rises with dose |  |
| [[Erlotinib (drug)]] 5 µM |  | 1.21× | +3.1 | 0.12 | 13/47 (HOP62, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.0 | 0.14 | 9/48 (HOP62, SW 900, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5789.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.264×, KATO III 0.254×, SW480 0.439×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1792 0.0592×, hTERT-HPNE 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LOX-IMVI 0.125×, C32 0.185×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Silodosin (drug)]] 5 µM in 1 line (C-33 A 0.0828×); [[Naproxen (drug)]] 0.05 µM in 1 line (SW48 0.0843×); [[Harringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.0923×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.611×** | -11.8 | 2e-29 | 38/47 (RKO, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.645×** | -7.2 | 2e-10 | 27/47 (A-427, NCI-H1792, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.696×** | -6.2 | 1e-07 | 27/47 (KATO III, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.729×** | -5.4 | 1e-05 | 22/47 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.744×** | -4.8 | 1e-04 | 22/45 (NCI-H1573, LS 180, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.763×** | -4.4 | 9e-04 | 21/47 (HepG2/C3A, AN3 CA, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.025 | 11/48 (HT-29, LoVo, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.823×** | -3.3 | 0.063 | 19/42 (NCI-H1573, KATO III, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 18.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H460 (line)]] | wt | 21.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.7) ⚠ cell-cycle shift, explains ~5% of this change | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RKO (line)]] | wt | 21.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -11.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[venetoclax (drug)]] 5 µM 0.0751× (z -9.0) |
| [[SW480 (line)]] | alt | 25.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.96× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[A-427 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -9.6) ⚠ cell-cycle shift, explains ~3% of this change |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0828× (z -11.0) |
| [[C32 (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H1792 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0592× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0923× (z -9.3) |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -8.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW48 (line)]] | wt | 19.3 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0843× (z -9.8) |
| [[A-172 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM115]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[SPRING1]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[RAB5C]] | +0.60 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CDK9]] | +0.59 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[FASTKD5]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[VAMP3]] | +0.58 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[BAG5]] | +0.58 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[ASB6]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ZDHHC5]] | +0.55 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ILRUN]] | +0.54 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[LRP10]] | +0.54 | +0.60 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTBP2]] | -0.50 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[ANKRD26]] | -0.50 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[LINC01473]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CEP290]] | -0.48 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.47 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[TCAF1]] | -0.46 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ZC3H12B]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TMEM127's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.360). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-14.5, -17.4); signed map (-49.3, -9.7). **Vector** length 81.0, 15.0% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +2.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.9 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -7.1 | -11.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.5 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.5 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 127 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,248,514-96,266,047 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20507, FLJ22257 |
| Matched by | ensembl_id |

**Function**, from UniProt [O75204](https://www.uniprot.org/uniprotkb/O75204) (Transmembrane protein 127):

> Controls cell proliferation acting as a negative regulator of TOR signaling pathway mediated by mTORC1. May act as a tumor suppressor.

**Summary**, from NCBI Gene [55654](https://www.ncbi.nlm.nih.gov/gene/55654):

> This gene encodes a transmembrane protein with four predicted transmembrane domains. The protein is associated with a subpopulation of vesicular organelles corresponding to early endosomal structures, with the Golgi, and with lysosomes, and may participate in protein trafficking between these structures. Mutations in this gene and several other genes cause pheochromocytomas. Alternatively spliced transcript variants encoding the same protein have been identified. [provided by RefSeq, Aug 2022]

**Accessions** — [HGNC:26038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26038) · Entrez [55654](https://www.ncbi.nlm.nih.gov/gene/55654) · UniProt [O75204](https://www.uniprot.org/uniprotkb/O75204) · Ensembl [ENSG00000135956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135956)

## Data

Gene col 5789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5789); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5789]; `tensor/DDL_lfc|DDL_z.npy` [5789]; `embed/gene_vectors.npy` [5789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5789 or target_col == 5789). Every well: [[TMEM127 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM127.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
