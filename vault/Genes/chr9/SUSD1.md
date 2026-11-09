---
symbol: "SUSD1"
type: "gene"
col: 2813
ensembl_id: "ENSG00000106868"
name: "sushi domain containing 1"
location: "9q31.3-q32"
module: 124
arm: "+"
pooled_cpm: 33.71
n_lines_expressing: 44
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# SUSD1

*sushi domain containing 1* — 9q31.3-q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.30× (z +6.8, q 6e-09, up in 24 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.406× (z -16.6, q 0e+00, down in 33 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02977]] (+0.83, fdr 7e-06, ⚠ read-through risk), [[AVEN]] (+0.65, fdr 2e-05), [[ZNF124]] (+0.62, fdr 6e-05), [[SLC2A9]] (+0.62, fdr 7e-05); moves opposite to [[SNAPC3]] (-0.62, fdr 5e-05), [[HACE1]] (-0.60, fdr 5e-05), [[POT1]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02977]] → it (grade C ⚠); 1 goes from it, the strongest it → [[SLIT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.8 | 6e-09 | 24/42 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.0 | 0.018 | 9/42 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.024 | 15/41 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.032 | 12/42 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.21×** | +3.4 | 0.077 | 10/40 (SW480, SNU-423, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.2 | 0.11 | 8/41 (SW 900, A498, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.11 | 2/42 (CFPAC-1, A549) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.11 | 7/41 (SW480, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.11 | 15/41 (A498, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2813.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.406×** | -16.6 | 0e+00 | 33/41 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.416×** | -16.1 | 0e+00 | 34/42 (RKO, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.434×** | -15.3 | 0e+00 | 31/42 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.556×** | -10.8 | 6e-25 | 31/40 (HT-29, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.598×** | -9.4 | 4e-19 | 24/42 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.491×** | -6.8 | 9e-10 | 25/42 (RKO, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.773×** | -6.7 | 2e-09 | 25/42 (COLO 205, A-172, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.730×** | -5.6 | 2e-06 | 21/39 (HepG2/C3A, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **0.747×** | -5.3 | 6e-06 | 21/38 (HOP62, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.744×** | -5.2 | 1e-05 | 21/42 (MIA PaCa-2, RKO, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.05 µM |  | **0.784×** | -4.5 | 4e-04 | 21/41 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.651×** | -4.1 | 0.002 | 17/38 (NCI-H1792, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 0.860× | -3.9 | 0.004 | 8/42 (NCI-H661, CFPAC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.873× | -3.5 | 0.017 | 12/42 (LOX-IMVI, COLO 205, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.822×** | -3.5 | 0.020 | 15/39 (A-172, NCI-H23, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.837× | -3.3 | 0.036 | 14/42 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Silodosin (drug)]] 5 µM |  | 0.839× | -3.1 | 0.061 | 8/40 (hTERT-HPNE, A498, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.844× | -3.0 | 0.075 | 11/41 (NCI-H661, SNU-423, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.732×** | -3.0 | 0.075 | 9/39 (J82, SHP-77, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 36.1 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -15.8) |
| [[RKO (line)]] | wt | 63.2 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -18.0) |
| [[COLO 205 (line)]] | alt | 163 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -19.0) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.150× (z -17.0) |
| [[HepG2_C3A (line)]] | wt | 107 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -14.9) |
| [[AsPC-1 (line)]] | alt | 29.0 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.173× (z -12.2) |
| [[HT-29 (line)]] | alt | 36.5 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.153× (z -14.6) |
| [[LoVo (line)]] | wt | 76.8 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.270× (z -13.7) |
| [[PANC-1 (line)]] | alt | 20.9 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -10.8) |
| [[SW480 (line)]] | alt | 29.8 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.152× (z -20.8) |
| [[HOP62 (line)]] | alt | 26.8 | 0 | 4 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.199× (z -13.5) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.306× (z -9.9) |
| [[J82 (line)]] | alt | 78.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 45.9 | 0 | 4 | — | [[Belinostat (drug)]] 0.5 µM 0.207× (z -12.2) |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.156× (z -13.7) |
| [[KATO III (line)]] | alt | 39.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.258× (z -10.4) |
| [[LS 180 (line)]] | wt | 46.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -10.6) |
| [[SW1417 (line)]] | alt | 41.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -10.5) |
| [[A-172 (line)]] | wt | 25.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.2) ⚠ cell-cycle shift, explains ~73% of this change |
| [[C32 (line)]] | wt | 11.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +9.7) ⚠ cell-cycle shift, explains ~73% of this change | [[Monocrotaline (drug)]] 0.05 µM 0.0993× (z -9.8) |
| [[A498 (line)]] | wt | 35.9 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.10× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 52.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -9.5) |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.120× (z -12.2) |
| [[H4 (line)]] | wt | 10.9 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0760× (z -8.7) |
| [[Hs 766T (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.142× (z -11.7) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change |
| [[Panc 03.27 (line)]] | alt | 41.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.140× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 60.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -10.4) |
| [[SW 900 (line)]] | alt | 42.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.206× (z -9.2) |
| [[SW48 (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0898× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 8.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.84 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.21 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.30 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02977]] | +0.83 | +0.78 / +0.74 | both halves | 7e-06 | ⚠ **readthrough risk**: LINC02977 lies 1.6 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[AVEN]] | +0.65 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ZNF124]] | +0.62 | +0.39 / +0.39 | both halves | 6e-05 |  |
| [[SLC2A9]] | +0.62 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[ARSB]] | +0.62 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[MMADHC-DT]] | +0.61 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[NEK10]] | +0.60 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ZNF876P]] | +0.59 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[SLC13A3]] | +0.59 | +0.42 / +0.30 | both halves | 2e-04 |  |
| [[SPON1-AS1]] | +0.59 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[RNPC3-DT]] | +0.59 | +0.42 / +0.22 | both halves | 6e-04 |  |
| [[ARRDC3-AS1]] | +0.59 | +0.30 / +0.43 | both halves | 2e-04 |  |
| [[MCF2]] | +0.58 | +0.41 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPC3]] | -0.62 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[HACE1]] | -0.60 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[POT1]] | -0.59 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[KBTBD3]] | -0.59 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[ARL6]] | -0.58 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ZNF14]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[ATG4C]] | -0.58 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ARL3]] | -0.58 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[PRMT9]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SKIC3]] | -0.57 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[KANTR]] | -0.57 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[THAP8]] | -0.57 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02977]] | C | LINC02977 activity raises SUSD1's level | lines that do not express LINC02977 (8) vs lines expressing it (42) | 3.43× lower at baseline in the lines without LINC02977 | 0.003 | ⚠ within organs, on part of the lines; also absent: SUSD1, FAM83G; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLIT2]] | B | SUSD1 activity raises SLIT2's level | lines that do not express SUSD1 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without SUSD1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ETS2, TCIRG1, SDC4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (7.7, -8.4); signed map (18.3, -0.5). **Vector** length 94.6, 21.3% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.4 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +0.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.8 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +1.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.3 | -10.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -6.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.5 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -16.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.9 | -4.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | sushi domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3-q32 — chr9:112,040,783-112,175,297 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP761E1824 |
| Gene groups (HGNC) | Sushi domain containing |
| Matched by | ensembl_id |

UniProt [Q6UWL2](https://www.uniprot.org/uniprotkb/Q6UWL2) carries no function annotation.

**Summary**, from NCBI Gene [64420](https://www.ncbi.nlm.nih.gov/gene/64420):

> Predicted to enable calcium ion binding activity. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25413) · Entrez [64420](https://www.ncbi.nlm.nih.gov/gene/64420) · UniProt [Q6UWL2](https://www.uniprot.org/uniprotkb/Q6UWL2) · Ensembl [ENSG00000106868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106868)

## Data

Gene col 2813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2813); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2813]; `tensor/DDL_lfc|DDL_z.npy` [2813]; `embed/gene_vectors.npy` [2813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2813 or target_col == 2813). Every well: [[SUSD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUSD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
