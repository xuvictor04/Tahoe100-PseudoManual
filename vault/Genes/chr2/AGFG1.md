---
symbol: "AGFG1"
type: "gene"
col: 10424
ensembl_id: "ENSG00000173744"
name: "ArfGAP with FG repeats 1"
location: "2q36.3"
module: 214
arm: "+"
pooled_cpm: 166.74
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/214"]
generated_by: "tahoemap"
---

# AGFG1

*ArfGAP with FG repeats 1* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.07× (z +11.3, q 7e-27, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.509× (z -10.1, q 3e-21, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.660× (z -9.2, q 1e-17, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KPNA1]] (+0.70, fdr 7e-06), [[HIF1A]] (+0.64, fdr 7e-06), [[FDX1]] (+0.59, fdr 1e-05); moves opposite to [[LINC00310]] (-0.52, fdr 3e-05), [[MRPS6]] (-0.50, fdr 4e-05), [[POLR3D]] (-0.49, fdr 1e-04).
> It is in [[Module 214]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.07×** | +11.3 | 7e-27 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.70×** | +10.7 | 5e-24 | 47/49 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.09×** | +9.2 | 9e-18 | 46/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +8.8 | 1e-16 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +7.8 | 7e-13 | 43/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +7.8 | 7e-13 | 43/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +7.7 | 2e-12 | 30/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +4.4 | 7e-04 | 30/48 (MIA PaCa-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.002 | 29/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.7 | 0.010 | 28/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.012 | 26/47 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.069 | 21/48 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.1 | 0.078 | 18/48 (PANC-1, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10424.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.509×** | -10.1 | 3e-21 | 39/44 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -9.2 | 1e-17 | 40/49 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.575×** | -8.6 | 1e-15 | 39/49 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.662×** | -6.4 | 2e-08 | 39/48 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.740×** | -4.5 | 7e-04 | 29/47 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.9 | 0.009 | 21/48 (Hs 766T, J82, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.792×** | -3.5 | 0.038 | 27/50 (NCI-H460, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.808×** | -3.3 | 0.059 | 25/48 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.870× | -3.1 | 0.13 | 8/48 (NCI-H2347, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 471 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -21.9) |
| [[SW480 (line)]] | alt | 98.8 | 9 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.10× (z +15.4) | — |
| [[PANC-1 (line)]] | alt | 87.4 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +16.5) | — |
| [[KATO III (line)]] | alt | 142 | 6 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 178 | 6 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.61× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.51× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -17.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 119 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +12.7) | — |
| [[NCI-H23 (line)]] | alt | 214 | 3 (1 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.34× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -10.0) |
| [[HS-578T (line)]] | alt | 189 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -19.1) |
| [[LS 180 (line)]] | wt | 158 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +13.9) | — |
| [[NCI-H2347 (line)]] | alt | 152 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -10.3) |
| [[A549 (line)]] | wt | 388 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -24.0) |
| [[C32 (line)]] | wt | 141 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 11.9× (z +13.2) | — |
| [[SW48 (line)]] | wt | 106 | 4 | 0 | [[TAK-901 (drug)]] 0.05 µM 5.01× (z +11.6) | — |
| [[A-172 (line)]] | wt | 139 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -16.4) |
| [[H4 (line)]] | wt | 116 | 3 | 0 | [[Digitoxin (drug)]] 0.5 µM 3.47× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 134 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +10.2) | — |
| [[J82 (line)]] | alt | 192 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 80.1 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.74× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 222 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -16.6) |
| [[NCI-H2030 (line)]] | alt | 251 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 136 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 5.67× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 170 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -12.1) |
| [[SW 900 (line)]] | alt | 115 | 2 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 184 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 195 | 2 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.70× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 211 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.34× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 125 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +11.3) | — |
| [[RKO (line)]] | wt | 115 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.77× (z +9.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.278× (z -12.5) ⚠ toxic |
| [[SW1417 (line)]] | alt | 187 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 224 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -17.5) |
| [[CFPAC-1 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 68.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.79× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -8.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 185 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.3) |
| [[SHP-77 (line)]] | alt | 135 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -10.2) |
| [[A-427 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 124 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 106 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 165 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA1]] | +0.70 | +0.61 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[HIF1A]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[FDX1]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[XPR1]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PPP4R1]] | +0.58 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[VAPA]] | +0.57 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[IFNGR1]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[B4GALT1]] | +0.55 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ARHGAP17]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PID1]] | +0.54 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[MRTFA]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[GGACT]] | +0.51 | +0.35 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00310]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MRPS6]] | -0.50 | -0.43 / -0.51 | both halves | 4e-05 |  |
| [[POLR3D]] | -0.49 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[ROPN1L]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 | same gene group |
| [[LRP2BP]] | -0.49 | -0.50 / -0.37 | both halves | 9e-05 |  |
| [[MPDU1]] | -0.48 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[FGF18]] | -0.46 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[MIR9-1HG]] | -0.46 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[LINC02936]] | -0.46 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[KLRA1P]] | -0.46 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[CCDC62]] | -0.45 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[TRIM72]] | -0.45 | -0.46 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 214]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.8, 17.8); signed map (-28.2, -17.2). **Vector** length 109, 38.5% of its response variance represented; |z| ≥ 3 in 1,323 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.5 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | -8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | -10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.3 | -0.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.9 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | -0.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.1 | +1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -9.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -1.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.6 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | +0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.4 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with FG repeats 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:227,472,152-227,561,217 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RIP, RAB; previously HRB |
| Gene groups (HGNC) | ArfGAPs; MicroRNA protein coding host genes |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P52594](https://www.uniprot.org/uniprotkb/P52594) (Arf-GAP domain and FG repeat-containing protein 1):

> Required for vesicle docking or fusion during acrosome biogenesis (By similarity). May play a role in RNA trafficking or localization. In case of infection by HIV-1, acts as a cofactor for viral Rev and promotes movement of Rev-responsive element-containing RNAs from the nuclear periphery to the cytoplasm. This step is essential for HIV-1 replication.

**Summary**, from NCBI Gene [3267](https://www.ncbi.nlm.nih.gov/gene/3267):

> The protein encoded by this gene is related to nucleoporins, a class of proteins that mediate nucleocytoplasmic transport. The encoded protein binds the activation domain of the human immunodeficiency virus Rev protein when Rev is assembled onto its RNA target, and is required for the nuclear export of Rev-directed RNAs. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2008]

**Accessions** — [HGNC:5175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5175) · Entrez [3267](https://www.ncbi.nlm.nih.gov/gene/3267) · UniProt [P52594](https://www.uniprot.org/uniprotkb/P52594) · Ensembl [ENSG00000173744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173744)

## Data

Gene col 10424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10424); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10424]; `tensor/DDL_lfc|DDL_z.npy` [10424]; `embed/gene_vectors.npy` [10424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10424 or target_col == 10424). Every well: [[AGFG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGFG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
