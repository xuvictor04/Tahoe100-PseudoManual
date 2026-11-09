---
symbol: "GFOD1"
type: "gene"
col: 7050
ensembl_id: "ENSG00000145990"
name: "Gfo/Idh/MocA-like oxidoreductase domain containing 1"
location: "6p24.1-p23"
module: 34
arm: "+"
pooled_cpm: 15.7
n_lines_expressing: 45
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 10
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# GFOD1

*Gfo/Idh/MocA-like oxidoreductase domain containing 1* — 6p24.1-p23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.50× (z +26.2, q 0e+00, up in 42 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Sunitinib (drug)]] 5 µM: 0.786× (z -3.7, q 0.077, down in 14 of 41 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (Hs 766T 0.228×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SNU-1 0.0718×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.265×); [[Ixazomib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.187×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF13]] (+0.62, fdr 2e-05), [[FUT4]] (+0.56, fdr 3e-05), [[DOCK9]] (+0.55, fdr 2e-05); moves opposite to [[PHC3]] (-0.55, fdr 2e-05), [[MCCC1]] (-0.52, fdr 3e-05), [[CHURC1-FNTB]] (-0.52, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[ENDOD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7050.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.50×** | +26.2 | 0e+00 | 42/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.94×** | +24.5 | 0e+00 | 41/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.84×** | +24.2 | 0e+00 | 41/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +19.5 | 0e+00 | 29/40 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.27×** | +18.2 | 0e+00 | 41/42 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.41×** | +13.5 | 1e-39 | 32/39 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +13.2 | 8e-38 | 28/43 (J82, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **4.27×** | +11.7 | 2e-29 | 37/43 (PANC-1, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +9.1 | 5e-18 | 25/41 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.71×** | +8.3 | 8e-15 | 25/42 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.57×** | +6.9 | 3e-10 | 25/42 (J82, HS-578T, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.59×** | +6.9 | 3e-10 | 26/41 (NCI-H460, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +6.5 | 4e-09 | 17/40 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +5.8 | 2e-07 | 19/39 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **1.44×** | +5.4 | 3e-06 | 14/37 (SW480, HOP62, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.8 | 5e-05 | 17/43 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.002 | 14/42 (SW480, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.003 | 10/39 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.003 | 10/40 (RKO, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7050.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (Hs 766T 0.228×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SNU-1 0.0718×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.265×); [[Ixazomib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.187×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.786×** | -3.7 | 0.077 | 14/41 (NCI-H1792, HepG2/C3A, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.636×** | -3.6 | 0.077 | 11/39 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 5.81 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 15.9× (z +12.5) | — |
| [[SW480 (line)]] | alt | 20.9 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 11.9 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.66× (z +17.1) | — |
| [[PANC-1 (line)]] | alt | 6.22 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 12.4× (z +14.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.234× (z -8.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[CFPAC-1 (line)]] | alt | 6.47 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.3× (z +10.4) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.138× (z -8.5) ⚠ toxic |
| [[J82 (line)]] | alt | 24.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.98× (z +12.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 7.03× (z +10.5) | [[Ixazomib (drug)]] 0.05 µM 0.187× (z -8.6) |
| [[A-172 (line)]] | wt | 7.03 | 3 | 0 | [[Belinostat (drug)]] 5 µM 10.5× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 5.60 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.59× (z +9.0) | — |
| [[LoVo (line)]] | wt | 16.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.75× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 24.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 7.88 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.7× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.16× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 36.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.16× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 6.39 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 16.6× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 20.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.59× (z +10.3) | — |
| [[A498 (line)]] | wt | 9.69 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +8.7) | — |
| [[A549 (line)]] | wt | 9.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 26.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 29.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.43× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.228× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 11.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.78× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 35.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 40.8 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.85× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0718× (z -9.4) |
| [[A-427 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF13]] | +0.62 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[FUT4]] | +0.56 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[DOCK9]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LRP8]] | +0.55 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[GATAD2A]] | +0.54 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[PPARGC1B]] | +0.54 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[STRIP2]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[TRAK1]] | +0.53 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[RAP1GAP2]] | +0.53 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[OTUD7A]] | +0.53 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[TIAM1]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PIP4K2A]] | +0.52 | +0.38 / +0.51 | both halves | 6e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC3]] | -0.55 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MCCC1]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[CHURC1-FNTB]] | -0.52 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[KRBOX4]] | -0.52 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[AKAP10]] | -0.51 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[LRRC27]] | -0.51 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[BBS1]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ZC3H7A]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[PMPCB]] | -0.50 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[N4BP2L2]] | -0.49 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[COG4]] | -0.49 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[CEP57]] | -0.49 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GFOD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RAP1GAP2]] | C | RAP1GAP2 activity raises GFOD1's level | lines that do not express RAP1GAP2 (4) vs lines expressing it (46) | 2.54× lower at baseline in the lines without RAP1GAP2 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRIF1, IFI30; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENDOD1]] | B | GFOD1 activity strengthens ENDOD1's drug response | lines that do not express GFOD1 (5) vs lines expressing it (41) | the lines without GFOD1 respond 0.60× as strongly (z diff +1.61); strongest at Homoharringtonine 5 µM: 1.08x vs 0.37x (z diff +7.4) | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MAST2]] | B | GFOD1 activity raises MAST2's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without GFOD1 | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[C1orf43]] | B | GFOD1 activity lowers C1orf43's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.34× higher at baseline in the lines without GFOD1 | 0.028 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[LRRC27]] | B | GFOD1 activity lowers LRRC27's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.42× higher at baseline in the lines without GFOD1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[FAR1]] | B | GFOD1 activity raises FAR1's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without GFOD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[CHURC1-FNTB]] | B | GFOD1 activity lowers CHURC1-FNTB's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.69× higher at baseline in the lines without GFOD1 | 0.053 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[BMP2K]] | B | GFOD1 activity raises BMP2K's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.58× lower at baseline in the lines without GFOD1 | 0.078 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[MFSD14B]] | B | GFOD1 activity raises MFSD14B's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.49× lower at baseline in the lines without GFOD1 | 0.080 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[ZC3H7A]] | B | GFOD1 activity raises ZC3H7A's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.29× lower at baseline in the lines without GFOD1 | 0.090 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[LTBP1]] | B | GFOD1 activity raises LTBP1's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 2.57× lower at baseline in the lines without GFOD1 | 0.0997 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.393). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.5, 35.0); signed map (-10.6, 44.3). **Vector** length 77.3, 15.1% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +8.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +13.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +18.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +13.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.8 | +4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +11.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | +9.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.1 | +1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -1.8 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | +1.7 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | Gfo/Idh/MocA-like oxidoreductase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.1-p23 — chr6:13,357,830-13,487,662 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20330, ADG-90; previously C6orf114 |
| Gene groups (HGNC) | Gfo/Idh/MocA-like oxidoreductase domain containing |
| Reactome | 4 pathways, smallest: RHOQ GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXC2](https://www.uniprot.org/uniprotkb/Q9NXC2) (Glucose-fructose oxidoreductase domain-containing protein 1):

> Probably catalytically inactive enzyme. Does not bind NAD or NADP.

**Summary**, from NCBI Gene [54438](https://www.ncbi.nlm.nih.gov/gene/54438):

> Enables identical protein binding activity. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21096) · Entrez [54438](https://www.ncbi.nlm.nih.gov/gene/54438) · UniProt [Q9NXC2](https://www.uniprot.org/uniprotkb/Q9NXC2) · Ensembl [ENSG00000145990](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145990)

## Data

Gene col 7050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7050); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7050]; `tensor/DDL_lfc|DDL_z.npy` [7050]; `embed/gene_vectors.npy` [7050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7050 or target_col == 7050). Every well: [[GFOD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GFOD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
