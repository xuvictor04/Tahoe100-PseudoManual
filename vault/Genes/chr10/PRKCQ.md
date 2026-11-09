---
symbol: "PRKCQ"
type: "gene"
col: 802
ensembl_id: "ENSG00000065675"
name: "protein kinase C theta"
location: "10p15.1"
module: 115
arm: "+"
pooled_cpm: 5.89
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# PRKCQ

*protein kinase C theta* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.02× (z +12.9, q 4e-35, up in 33 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.553× (z -7.3, q 1e-10, down in 17 of 40 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.582× (z -7.0, q 8e-10, down in 17 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00937]] (+0.73, fdr 7e-06), [[ARHGAP44]] (+0.66, fdr 1e-05), [[EMID1]] (+0.63, fdr 8e-06); moves opposite to [[LMLN]] (-0.48, fdr 6e-04), [[PPP1R7]] (-0.48, fdr 5e-04), [[SLC30A9]] (-0.46, fdr 2e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[BTNL9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 802.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +12.9 | 4e-35 | 33/42 (HEC-1-A, HT-29, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +10.1 | 2e-21 | 18/33 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +8.3 | 3e-14 | 1/8 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +8.1 | 8e-14 | 22/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +8.1 | 8e-14 | 24/40 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +7.3 | 3e-11 | 4/16 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +7.0 | 2e-10 | 16/43 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +6.7 | 2e-09 | 20/43 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.49×** | +5.2 | 1e-05 | 16/43 (PANC-1, SHP-77, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +4.9 | 4e-05 | 1/10 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.43×** | +4.6 | 2e-04 | 14/43 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.38×** | +4.1 | 0.002 | 5/31 (NCI-H460, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.37×** | +3.9 | 0.003 | 9/23 (LoVo, SW 900, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.77×** | +3.9 | 0.005 | 4/14 (A549, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.33×** | +3.7 | 0.007 | 10/42 (A549, LoVo, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.008 | 2/30 (NCI-H460, SNU-423) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.008 | 9/39 (A549, SW480, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +3.3 | 0.033 | 5/41 (HEC-1-A, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.050 | 2/38 (LoVo, SNU-1) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 802.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.553×** | -7.3 | 1e-10 | 17/40 (COLO 205, KATO III, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -7.0 | 8e-10 | 17/42 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.641×** | -5.7 | 2e-06 | 21/31 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.666×** | -5.2 | 2e-05 | 21/44 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -4.8 | 2e-04 | 10/45 (HepG2/C3A, SNU-423, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.783×** | -4.4 | 9e-04 | 19/38 (NCI-H2030, COLO 205, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.729×** | -4.1 | 0.004 | 12/37 (A549, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.744×** | -3.8 | 0.010 | 7/43 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.746×** | -3.8 | 0.011 | 13/42 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.754×** | -3.6 | 0.016 | 11/40 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.789× | -3.0 | 0.12 | 11/43 (A549, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 19.9 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.9) ⚠ cell-cycle shift, explains ~99% of this change |
| [[LoVo (line)]] | wt | 14.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0891× (z -15.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 9.88 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -13.5) |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.9) ⚠ cell-cycle shift, explains ~99% of this change |
| [[HEC-1-A (line)]] | alt | 14.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 19.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -14.4) ⚠ cell-cycle shift, explains ~99% of this change |
| [[RKO (line)]] | wt | 14.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -8.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -8.9) |
| [[SW48 (line)]] | wt | 13.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0662× (z -9.8) |
| [[KATO III (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.212× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 3.88 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0818× (z -8.7) ⚠ transcription drop; unreliable plate only |
| [[NCI-H23 (line)]] | alt | 7.70 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0848× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0402× (z -13.5) |
| [[SW 900 (line)]] | alt | 8.09 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00937]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ARHGAP44]] | +0.66 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[EMID1]] | +0.63 | +0.65 / +0.57 | both halves | 8e-06 |  |
| [[TMEM98]] | +0.59 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[SUSD4]] | +0.57 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SLC26A5]] | +0.57 | +0.44 / +0.62 | both halves | 3e-05 | pathway: Sensory Perception |
| [[PLLP]] | +0.56 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[TMEM150C]] | +0.56 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[SBK1]] | +0.55 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SLC27A2]] | +0.54 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[TTPA]] | +0.54 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ENTPD1]] | +0.53 | +0.34 / +0.63 | both halves | 1e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMLN]] | -0.48 | -0.23 / -0.48 | both halves | 6e-04 |  |
| [[PPP1R7]] | -0.48 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[SLC30A9]] | -0.46 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[FCF1]] | -0.45 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[MCPH1-AS1]] | -0.44 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[LMBRD2]] | -0.44 | -0.21 / -0.41 | both halves | 7e-04 |  |
| [[MPV17]] | -0.44 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[ZNF548]] | -0.43 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[RO60]] | -0.43 | -0.24 / -0.46 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTNL9]] | B | BTNL9 activity raises PRKCQ's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.27× lower at baseline in the lines without BTNL9 | 0.014 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[SLC27A2]] | B | SLC27A2 activity raises PRKCQ's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 2.07× lower at baseline in the lines without SLC27A2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| [[TMEM98]] | B | TMEM98 activity raises PRKCQ's level | lines that do not express TMEM98 (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without TMEM98 | 0.083 | ⚠ within organs, on part of the lines; also absent: PGAP4, EDARADD, RPS6KA6; maybe low, not absent |
| [[GPC4]] | B | GPC4 activity raises PRKCQ's level | lines that do not express GPC4 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without GPC4 | 0.088 | ⚠ within organs, on part of the lines; also absent: KCNK5, NTN1, FUT3 |
| [[EMID1]] | B | EMID1 activity raises PRKCQ's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.65× lower at baseline in the lines without EMID1 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[PALS2]] | C | PALS2 activity strengthens PRKCQ's drug response | lines that do not express PALS2 (3) vs lines expressing it (41) | the lines without PALS2 respond 0.69× as strongly (z diff +0.46); strongest at Panobinostat 0.5 µM: 0.70x vs 1.78x (z diff +3.8) | 0.073 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.6, 37.5); signed map (53.2, 30.4). **Vector** length 54.4, 7.40% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +12.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +10.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +3.0 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.8 | -7.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -5.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.4 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -0.9 | -0.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.9 | -0.7 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -0.8 | -0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase C theta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:6,427,143-6,580,301 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PKCθ |
| Gene groups (HGNC) | C2 domain containing protein kinases; Protein kinase C family |
| Reactome | 30 pathways, smallest: Inactivation, recovery and regulation of the phototransduction cascade; The phototransduction cascade; Effects of PIP2 hydrolysis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04759](https://www.uniprot.org/uniprotkb/Q04759) (Protein kinase C theta type):

> Calcium-independent, phospholipid- and diacylglycerol (DAG)-dependent serine/threonine-protein kinase that mediates non-redundant functions in T-cell receptor (TCR) signaling, including T-cells activation, proliferation, differentiation and survival, by mediating activation of multiple transcription factors such as NF-kappa-B, JUN, NFATC1 and NFATC2. In TCR-CD3/CD28-co-stimulated T-cells, is required for the activation of NF-kappa-B and JUN, which in turn are essential for IL2 production, and …

**Summary**, from NCBI Gene [5588](https://www.ncbi.nlm.nih.gov/gene/5588):

> Protein kinase C (PKC) is a family of serine- and threonine-specific protein kinases that can be activated by calcium and the second messenger diacylglycerol. PKC family members phosphorylate a wide variety of protein targets and are known to be involved in diverse cellular signaling pathways. PKC family members also serve as major receptors for phorbol esters, a class of tumor promoters. Each member of the PKC family has a specific expression profile and is believed to play a distinct role. …

**Accessions** — [HGNC:9410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9410) · Entrez [5588](https://www.ncbi.nlm.nih.gov/gene/5588) · UniProt [Q04759](https://www.uniprot.org/uniprotkb/Q04759) · Ensembl [ENSG00000065675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065675)

## Data

Gene col 802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 802); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 802]; `tensor/DDL_lfc|DDL_z.npy` [802]; `embed/gene_vectors.npy` [802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 802 or target_col == 802). Every well: [[PRKCQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKCQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
