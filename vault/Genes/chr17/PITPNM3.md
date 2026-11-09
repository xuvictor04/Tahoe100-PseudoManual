---
symbol: "PITPNM3"
type: "gene"
col: 1672
ensembl_id: "ENSG00000091622"
name: "PITPNM family member 3"
location: "17p13.2-p13.1"
module: 73
arm: "+"
pooled_cpm: 12.03
n_lines_expressing: 45
n_dd_up: 1
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 23
direction_downstream: 1
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# PITPNM3

*PITPNM family member 3* — 17p13.2-p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 2.24× (z +10.6, q 1e-23, up in 32 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 9.45×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (SW480 4.24×); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.94×; ⚠ position not correctable); [[Trametinib (drug)]] 0.5 µM in 1 line (NCI-H460 4.99×); [[Trametinib (drug)]] 0.05 µM in 1 line (NCI-H460 3.94×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.564× (z -7.6, q 2e-11, down in 22 of 42 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.629× (z -6.1, q 3e-07, down in 19 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO18A]] (+0.56, fdr 1e-05), [[SEPTIN9-DT]] (+0.56, fdr 3e-05), [[ARHGAP23]] (+0.55, fdr 2e-05); moves opposite to [[UHRF2]] (-0.47, fdr 9e-05), [[RPP21]] (-0.45, fdr 7e-05), [[FBXO17]] (-0.44, fdr 1e-04).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[LGR6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SEPTIN9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1672.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 9.45×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (SW480 4.24×); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.94×; ⚠ position not correctable); [[Trametinib (drug)]] 0.5 µM in 1 line (NCI-H460 4.99×); [[Trametinib (drug)]] 0.05 µM in 1 line (NCI-H460 3.94×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.24×** | +10.6 | 1e-23 | 32/40 (SW480, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.32× | +3.5 | 0.11 | 5/18 (SW 900, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 1.19× | +3.2 | 0.19 | 5/41 (LS 180, J82, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.28× | +3.2 | 0.19 | 9/39 (NCI-H460, HOP62, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.28× | +3.1 | 0.19 | 8/38 (HS-578T, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1672.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.564×** | -7.6 | 2e-11 | 22/42 (LoVo, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -6.1 | 3e-07 | 19/41 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.636×** | -6.0 | 5e-07 | 18/38 (A549, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.643×** | -5.8 | 7e-07 | 23/42 (LoVo, Hs 766T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.633×** | -5.8 | 7e-07 | 18/32 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.647×** | -5.8 | 8e-07 | 20/42 (LoVo, KATO III, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.661×** | -5.3 | 1e-05 | 19/40 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.681×** | -5.1 | 3e-05 | 20/42 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.669×** | -5.0 | 3e-05 | 13/38 (SW 900, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.689×** | -4.9 | 5e-05 | 18/42 (LoVo, Hs 766T, …) | two highest doses | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.544×** | -4.2 | 0.001 | 15/34 (LoVo, HCT15, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.735×** | -4.1 | 0.002 | 20/40 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.738×** | -4.0 | 0.003 | 16/42 (RPMI-7951, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.562×** | -4.0 | 0.003 | 13/40 (KATO III, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.750×** | -3.8 | 0.005 | 17/39 (HOP62, NCI-H460, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.606×** | -3.5 | 0.018 | 11/36 (LoVo, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.772×** | -3.4 | 0.020 | 9/41 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.788×** | -3.1 | 0.048 | 8/36 (SW 900, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1672. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 38.5 | 0 | 12 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -17.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[4EGI-1 (drug)]] 5 µM 0.0636× (z -9.5) |
| [[LoVo (line)]] | wt | 42.8 | 0 | 10 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -18.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H460 (line)]] | wt | 8.67 | 5 (1 ⚠) | 3 (3 ⚠) | [[Trametinib (drug)]] 0.5 µM 4.99× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -11.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 46.9 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -19.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 8.03 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.45× (z +14.4) ⚠ cell-cycle shift, would explain all of this change | [[Hydroxyurea (drug)]] 0.05 µM 0.132× (z -8.5) |
| [[KATO III (line)]] | alt | 34.1 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -15.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.107× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 4.80 | 0 | 4 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0912× (z -9.6) |
| [[BT-474 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.0820× (z -8.6) |
| [[J82 (line)]] | alt | 23.3 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0985× (z -13.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 7.34 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0603× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.94× (z +10.8) ⚠ position not correctable | — |
| [[RPMI-7951 (line)]] | alt | 5.27 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0617× (z -8.9) |
| [[SW480 (line)]] | alt | 11.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.24× (z +10.9) | — |
| [[A-427 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1672), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO18A]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[SEPTIN9-DT]] | +0.56 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[ARHGAP23]] | +0.55 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SLC22A3]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CALB1]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[MYO16-AS1]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[MMP28]] | +0.51 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[TRABD2A]] | +0.50 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ELF4]] | +0.49 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[UNC13D]] | +0.49 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[TPTEP1-1]] | +0.49 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[HR]] | +0.49 | +0.51 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UHRF2]] | -0.47 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[RPP21]] | -0.45 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[FBXO17]] | -0.44 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[TMEM158]] | -0.42 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[POLR2G]] ⚠ | -0.42 | -0.32 / -0.39 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[WDR54]] | -0.42 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[CCDC107]] | -0.41 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[ZNHIT3]] | -0.40 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[STC1]] | -0.40 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[NIPSNAP2]] | -0.40 | -0.37 / -0.37 | both halves | 7e-05 |  |
| [[GEMIN8]] | -0.39 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[BMS1P1]] | -0.39 | -0.41 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGR6]] | B | LGR6 activity raises PITPNM3's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 2.08× lower at baseline in the lines without LGR6 | 0.009 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2 |
| [[LINC02582]] | B | LINC02582 activity raises PITPNM3's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.30× lower at baseline in the lines without LINC02582 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[LINC02582]] | B | LINC02582 activity strengthens PITPNM3's drug response | lines that do not express LINC02582 (35) vs lines expressing it (7) | the lines without LINC02582 respond 0.43× as strongly (z diff +2.46); strongest at Harringtonine 5 µM: 0.67x vs 0.30x (z diff +4.8) | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; target measured in part of the lines; artifact flags |
| [[MUC2]] | B | MUC2 activity raises PITPNM3's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 2.44× lower at baseline in the lines without MUC2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4 |
| [[KRT86]] | B | KRT86 activity raises PITPNM3's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without KRT86 | 0.023 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[KRT16]] | B | KRT16 activity raises PITPNM3's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 1.84× lower at baseline in the lines without KRT16 | 0.032 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[MMP28]] | B | MMP28 activity raises PITPNM3's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.43× lower at baseline in the lines without MMP28 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[FGF9]] | B | FGF9 activity raises PITPNM3's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 1.78× lower at baseline in the lines without FGF9 | 0.050 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[CALB1]] | B | CALB1 activity raises PITPNM3's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 2.10× lower at baseline in the lines without CALB1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588 |
| [[LINC01133]] | B | LINC01133 activity strengthens PITPNM3's drug response | lines that do not express LINC01133 (30) vs lines expressing it (12) | the lines without LINC01133 respond 0.57× as strongly (z diff +1.35); strongest at Panobinostat 0.5 µM: 0.67x vs 0.26x (z diff +4.2) | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1; target measured in part of the lines; artifact flags |
| [[MUC2]] | B | MUC2 activity strengthens PITPNM3's drug response | lines that do not express MUC2 (36) vs lines expressing it (6) | the lines without MUC2 respond 0.47× as strongly (z diff +2.18); strongest at Panobinostat 0.5 µM: 0.59x vs 0.22x (z diff +5.0) | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; target measured in part of the lines; artifact flags |
| [[KRT6A]] | B | KRT6A activity strengthens PITPNM3's drug response | lines that do not express KRT6A (35) vs lines expressing it (7) | the lines without KRT6A respond 0.52× as strongly (z diff +1.83); strongest at Panobinostat 0.5 µM: 0.59x vs 0.25x (z diff +4.2) | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN9]] | B | PITPNM3 activity lowers SEPTIN9's level | lines that do not express PITPNM3 (5) vs lines expressing it (45) | 1.82× higher at baseline in the lines without PITPNM3 | 0.040 | ⚠ within organs, on part of the lines; also absent: DOK4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.3, 48.2); signed map (68.7, 6.7). **Vector** length 79.3, 14.7% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.4 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.2 | -3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | -0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.4 | -6.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.3 | -1.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | PITPNM family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2-p13.1 — chr17:6,451,263-6,556,555 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NIR1, RDGBA3, ACKR6; previously CORD5 |
| Gene groups (HGNC) | Phosphatidylinositol transfer proteins |
| Reactome | 4 pathways, smallest: Synthesis of PI; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZ71](https://www.uniprot.org/uniprotkb/Q9BZ71) (Membrane-associated phosphatidylinositol transfer protein 3):

> Catalyzes the transfer of phosphatidylinositol and phosphatidylcholine between membranes (in vitro) (By similarity). Binds calcium ions.

**Summary**, from NCBI Gene [83394](https://www.ncbi.nlm.nih.gov/gene/83394):

> This gene encodes a member of a family of membrane-associated phosphatidylinositol transfer domain-containing proteins. The calcium-binding protein has phosphatidylinositol (PI) transfer activity and interacts with the protein tyrosine kinase PTK2B (also known as PYK2). The protein is homologous to a Drosophila protein that is implicated in the visual transduction pathway in flies. Mutations in this gene result in autosomal dominant cone dystrophy. Multiple transcript variants encoding …

**Accessions** — [HGNC:21043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21043) · Entrez [83394](https://www.ncbi.nlm.nih.gov/gene/83394) · UniProt [Q9BZ71](https://www.uniprot.org/uniprotkb/Q9BZ71) · Ensembl [ENSG00000091622](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091622)

## Data

Gene col 1672: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1672); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1672, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1672]; `tensor/DDL_lfc|DDL_z.npy` [1672]; `embed/gene_vectors.npy` [1672]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1672 or target_col == 1672). Every well: [[PITPNM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITPNM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
