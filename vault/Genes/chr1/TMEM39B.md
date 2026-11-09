---
symbol: "TMEM39B"
type: "gene"
col: 4296
ensembl_id: "ENSG00000121775"
name: "transmembrane protein 39B"
location: "1p35.2"
module: 103
arm: "+"
pooled_cpm: 17.15
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# TMEM39B

*transmembrane protein 39B* — 1p35.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 3.54×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 2.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.508× (z -10.9, q 7e-25, down in 23 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.702× (z -5.7, q 2e-06, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM2B]] (+0.58, fdr 1e-05), [[STAG3]] (+0.57, fdr 2e-05), [[PFKFB4]] (+0.56, fdr 1e-05); moves opposite to [[GTF2F2]] (-0.54, fdr 4e-05), [[MAP7]] (-0.51, fdr 5e-05), [[PTPRK]] (-0.47, fdr 3e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ANXA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4296.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 3.54×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 2.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 1.24× | +3.6 | 0.17 | 17/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.20 | 3/48 (Hs 766T, MIA PaCa-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4296.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.508×** | -10.9 | 7e-25 | 23/27 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.588×** | -8.9 | 2e-16 | 26/40 (SHP-77, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.622×** | -7.4 | 4e-11 | 21/36 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -5.7 | 2e-06 | 21/48 (PANC-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -5.1 | 4e-05 | 19/48 (SW 900, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -5.0 | 5e-05 | 19/46 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.749×** | -4.8 | 1e-04 | 21/48 (C32, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.817×** | -4.7 | 2e-04 | 23/48 (SNU-423, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.796×** | -3.8 | 0.008 | 22/47 (H4, NCI-H2347, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.656×** | -3.7 | 0.013 | 12/44 (RPMI-7951, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.800×** | -3.6 | 0.017 | 17/48 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.865× | -3.4 | 0.034 | 9/48 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.826×** | -3.2 | 0.058 | 15/48 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.832×** | -3.1 | 0.087 | 7/48 (HCT15, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 27.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -9.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 27.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -9.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Bendamustine (drug)]] 5 µM 0.138× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 21.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 17.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0540× (z -21.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -9.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -9.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.5 µM 0.0686× (z -8.5) |
| [[C32 (line)]] | wt | 30.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.160× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~86% of this change |
| [[COLO 205 (line)]] | alt | 8.06 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0803× (z -9.0) |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -9.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -10.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -11.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -9.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 11.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -12.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.220× (z -9.2) |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -9.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 14.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.49× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM2B]] | +0.58 | +0.53 / +0.51 | both halves | 1e-05 | same gene group |
| [[STAG3]] | +0.57 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[PFKFB4]] | +0.56 | +0.57 / +0.57 | both halves | 1e-05 | same gene group |
| [[IKZF4]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[PPFIA3]] | +0.55 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[TMEM145]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[WDR54]] | +0.53 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[PPFIA4]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[ABCB9]] | +0.51 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ATP8B3]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[ACADS]] | +0.49 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RARA]] | +0.49 | +0.44 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2F2]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[MAP7]] | -0.51 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[PTPRK]] | -0.47 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ENOX2]] | -0.45 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[SH3D19]] | -0.44 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ARAP2]] | -0.43 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[ANXA3]] | -0.43 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[MTAP]] | -0.43 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[NDUFAF2]] | -0.43 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[PDCD6IP-DT]] | -0.42 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[LINC02474]] | -0.41 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[LINC02595]] | -0.41 | -0.27 / -0.40 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA3]] | B | ANXA3 activity lowers TMEM39B's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 1.64× higher at baseline in the lines without ANXA3 | 0.005 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[APLN]] | B | APLN activity raises TMEM39B's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.23× lower at baseline in the lines without APLN | 0.008 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BRSK1]] | B | BRSK1 activity raises TMEM39B's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without BRSK1 | 0.057 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[ARAP2]] | B | ARAP2 activity lowers TMEM39B's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 1.55× higher at baseline in the lines without ARAP2 | 0.067 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[TOP2A]] | B | TOP2A activity raises TMEM39B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP7]] | B | MAP7 activity lowers TMEM39B's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 1.48× higher at baseline in the lines without MAP7 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[ICAM5]] | B | ICAM5 activity raises TMEM39B's level | lines that do not express ICAM5 (14) vs lines expressing it (36) | 1.39× lower at baseline in the lines without ICAM5 | 0.092 | ⚠ within organs, on part of the lines; also absent: MDFIC, VIM, CAV1; maybe low, not absent |
| [[CNTNAP1]] | C | CNTNAP1 activity raises TMEM39B's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without CNTNAP1 | 0.006 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |
| [[WDR54]] | C | WDR54 activity raises TMEM39B's level | lines that do not express WDR54 (4) vs lines expressing it (46) | 1.81× lower at baseline in the lines without WDR54 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: COPZ2, CNTLN, KLF9; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.3, -19.6); signed map (-32.8, 33.7). **Vector** length 66.9, 10.4% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.2 | +2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~86% of this change | +2.2 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | -0.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | -0.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.4 | +0.6 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.2 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -1.9 | -4.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 39B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:32,072,031-32,102,866 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10315 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZU3](https://www.uniprot.org/uniprotkb/Q9GZU3) (Transmembrane protein 39B):

> May protect the cells against DNA damage caused by exposure to the cold-warming stress and facilitates tissue damage repair during the recovery phase.

**Summary**, from NCBI Gene [55116](https://www.ncbi.nlm.nih.gov/gene/55116):

> Predicted to be located in endoplasmic reticulum membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25510) · Entrez [55116](https://www.ncbi.nlm.nih.gov/gene/55116) · UniProt [Q9GZU3](https://www.uniprot.org/uniprotkb/Q9GZU3) · Ensembl [ENSG00000121775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121775)

## Data

Gene col 4296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4296); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4296]; `tensor/DDL_lfc|DDL_z.npy` [4296]; `embed/gene_vectors.npy` [4296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4296 or target_col == 4296). Every well: [[TMEM39B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM39B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
