---
symbol: "PCNA"
type: "gene"
col: 5353
ensembl_id: "ENSG00000132646"
name: "proliferating cell nuclear antigen"
location: "20p12.3"
module: 6
arm: "+"
pooled_cpm: 30.15
n_lines_expressing: 48
n_dd_up: 31
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PCNA

*proliferating cell nuclear antigen* — 20p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (22 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.73× (z +13.1, q 2e-36, up in 42 of 43 measured lines) ⚠ toxic; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.60× (z +6.8, q 4e-10, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.468× (z -7.9, q 2e-12, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYMS]] (+0.78, fdr 7e-06), [[FAM111B]] (+0.73, fdr 7e-06), [[MCM4]] (+0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 22 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5353.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **3.73×** | +13.1 | 2e-36 | 42/43 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **3.01×** | +11.4 | 2e-27 | 43/46 (A549, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.09×** | +10.8 | 9e-25 | 35/45 (A549, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **2.69×** | +10.2 | 2e-22 | 43/46 (SW1417, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.31×** | +8.6 | 7e-16 | 38/46 (AsPC-1, HepG2/C3A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.14×** | +7.9 | 4e-13 | 41/45 (RKO, A549, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **2.19×** | +7.8 | 5e-13 | 40/45 (A549, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **2.15×** | +7.6 | 2e-12 | 39/46 (A549, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.02×** | +7.0 | 2e-10 | 25/35 (SNU-423, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.96×** | +7.0 | 2e-10 | 29/43 (A549, SNU-423, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.8 | 4e-10 | 36/46 (A549, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.87×** | +6.0 | 1e-07 | 26/40 (SNU-423, PANC-1, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.71×** | +5.5 | 1e-06 | 29/45 (A549, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~88% of this change | **1.67×** | +5.1 | 1e-05 | 29/45 (C32, HOP62, …) | top dose only | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.62×** | +4.8 | 8e-05 | 28/45 (RKO, A549, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.46×** | +3.9 | 0.003 | 23/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.025 | 17/46 (HepG2/C3A, A498, …) | top dose only |  |
| [[Irinotecan (drug)]] 5 µM |  | **1.82×** | +3.2 | 0.028 | 14/46 (RKO, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.043 | 20/46 (A549, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.38×** | +3.1 | 0.047 | 17/46 (RKO, A-427, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +2.9 | 0.061 | 16/46 (A549, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +2.8 | 0.088 | 16/46 (C32, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5353.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.468×** | -7.9 | 2e-12 | 37/46 (NCI-H23, A-172, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.719×** | -4.8 | 3e-04 | 27/46 (COLO 205, HCT15, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.559×** | -4.3 | 0.003 | 25/46 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.751×** | -4.2 | 0.003 | 25/46 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.646×** | -4.1 | 0.004 | 24/46 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.648×** | -4.1 | 0.004 | 24/46 (A498, A-427, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.685×** | -3.8 | 0.012 | 22/45 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.644×** | -3.3 | 0.075 | 16/46 (NCI-H23, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.733×** | -3.2 | 0.075 | 15/45 (hTERT-HPNE, RKO, …) | rises with dose | low cells (technical?) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.558×** | -3.2 | 0.085 | 15/46 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.808×** | -3.1 | 0.085 | 19/46 (RKO, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.50 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 33.3 | 9 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +15.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 6.63× (z +11.6) | — |
| [[J82 (line)]] | alt | 60.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 23.6 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.99× (z +11.7) ⚠ toxic; cell-cycle shift, explains ~34% of this change | — |
| [[RKO (line)]] | wt | 58.4 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.2) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[A-172 (line)]] | wt | 37.3 | 1 (1 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.27× (z +9.9) ⚠ toxic; cell-cycle shift, explains ~34% of this change | [[Auranofin (drug)]] 5 µM 0.0852× (z -15.3) |
| [[C32 (line)]] | wt | 25.6 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.85× (z +10.5) ⚠ toxic; cell-cycle shift, explains ~34% of this change | — |
| [[HepG2_C3A (line)]] | wt | 24.7 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +12.2) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[LoVo (line)]] | wt | 28.1 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +12.1) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[LS 180 (line)]] | wt | 42.8 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.49× (z +9.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H23 (line)]] | alt | 37.2 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0757× (z -15.6) |
| [[SNU-423 (line)]] | alt | 16.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.50× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 23.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.77× (z +8.9) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[A-427 (line)]] | wt | 51.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.152× (z -12.7) |
| [[A498 (line)]] | wt | 43.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.38× (z +8.9) ⚠ toxic; cell-cycle shift, explains ~34% of this change | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.03× (z +8.6) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.167× (z -10.0) |
| [[HT-29 (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.41× (z +9.6) ⚠ toxic; cell-cycle shift, explains ~34% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +8.8) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[LOX-IMVI (line)]] | wt | 28.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.33× (z +9.5) ⚠ toxic; cell-cycle shift, explains ~34% of this change | — |
| [[SNU-1 (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 9.30× (z +8.7) ⚠ toxic; cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 54.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.80× (z +11.9) ⚠ toxic; cell-cycle shift, explains ~34% of this change | — |
| [[AN3 CA (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYMS]] | +0.78 | +0.81 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 913 |
| [[FAM111B]] | +0.73 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[MCM4]] | +0.71 | +0.80 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 965 |
| [[E2F2]] | +0.70 | +0.75 / +0.65 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins |
| [[E2F8]] | +0.70 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CLSPN]] | +0.70 | +0.75 / +0.66 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 597 |
| [[MCM10]] | +0.69 | +0.75 / +0.67 | both halves | 7e-06 | pathway: DNA Replication; STRING 674 |
| [[GINS4]] | +0.69 | +0.68 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[DYNC2I2]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[ZNF367]] | +0.69 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[HELLS]] | +0.68 | +0.79 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 494 |
| [[E2F1]] | +0.68 | +0.76 / +0.64 | both halves | 7e-06 | pathway: G0 and Early G1; STRING 697 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PCNA's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.3% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TCF19]] | B | TCF19 activity raises PCNA's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.38× lower at baseline in the lines without TCF19 | 0.011 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises PCNA's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.51× lower at baseline in the lines without CDC25A | 0.026 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers PCNA's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MCM10]] | C | MCM10 activity raises PCNA's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.78× lower at baseline in the lines without MCM10 | 0.006 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[ZNF367]] | C | ZNF367 activity raises PCNA's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.51× lower at baseline in the lines without ZNF367 | 0.041 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent; co-absent with the target |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises PCNA's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 3.46× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[MCM2]] | C | MCM2 activity raises PCNA's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 2.16× lower at baseline in the lines without MCM2 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent |
| [[TP53]] | C | TP53 activity strengthens PCNA's drug response | recorded loss-of-function mutation of TP53 in 29 lines vs 17 not recorded | the TP53-altered lines respond 0.73× as strongly (z diff +1.39); strongest at Idarubicin (hydrochloride) 5 µM: 1.65x vs 2.65x (z diff +3.3) | 0.434 over the table, 0.019 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.4, -44.7); signed map (-38.5, -46.4). **Vector** length 120, 41.1% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cell Cycle Checkpoints* (reactome, mean cos +0.54 to 45); *Activation of the pre-replicative complex* (reactome, mean cos +0.55 to 22); *Activation of ATR in response to replication stress* (reactome, mean cos +0.58 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +7.8 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.2 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | +5.6 | +13.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +5.0 | +4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +4.9 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +6.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.5 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +2.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -11.2 | -7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | -5.7 | -4.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -4.7 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.5 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | proliferating cell nuclear antigen |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.3 — chr20:5,114,953-5,126,626 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | DNA_REPAIR, P53_PATHWAY, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 64 pathways, smallest: Leading Strand Synthesis; Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta); Mismatch repair (MMR) directed by MSH2:MSH6 (MutSalpha) |
| Matched by | ensembl_id |

**Function**, from UniProt [P12004](https://www.uniprot.org/uniprotkb/P12004) (DNA sliding clamp PCNA):

> Confers DNA tethering and processivity to DNA polymerases and other proteins. Auxiliary protein of DNA polymerase delta and epsilon, is involved in the control of DNA replication by increasing the polymerases' processivity during elongation of the leading strand. Induces a robust stimulatory effect on the 3'-5' exonuclease and 3'-phosphodiesterase, but not apurinic-apyrimidinic (AP) endonuclease, APEX2 activities. Has to be loaded onto DNA in order to be able to stimulate APEX2. Plays a key …

**Summary**, from NCBI Gene [5111](https://www.ncbi.nlm.nih.gov/gene/5111):

> The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have been found for this gene. Pseudogenes of this gene have been described on chromosome 4 and on the X …

**Accessions** — [HGNC:8729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8729) · Entrez [5111](https://www.ncbi.nlm.nih.gov/gene/5111) · UniProt [P12004](https://www.uniprot.org/uniprotkb/P12004) · Ensembl [ENSG00000132646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132646)

## Data

Gene col 5353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5353); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5353]; `tensor/DDL_lfc|DDL_z.npy` [5353]; `embed/gene_vectors.npy` [5353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5353 or target_col == 5353). Every well: [[PCNA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCNA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
