---
symbol: "PGBD1"
type: "gene"
col: 6004
ensembl_id: "ENSG00000137338"
name: "piggyBac transposable element derived 1"
location: "6p22.1"
module: 129
arm: "+"
pooled_cpm: 15.04
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# PGBD1

*piggyBac transposable element derived 1* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.68× (z +9.6, q 6e-19, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.645× (z -11.4, q 2e-27, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF329]] (+0.65, fdr 1e-05), [[PDRG1]] (+0.61, fdr 1e-05), [[KBTBD6]] (+0.61, fdr 3e-05); moves opposite to [[STT3B]] (-0.58, fdr 1e-05), [[XNDC1N]] (-0.57, fdr 5e-05), [[PCAT1]] (-0.54, fdr 3e-05).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ZIM2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6004.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +9.6 | 6e-19 | 35/44 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +8.6 | 3e-15 | 25/40 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +7.4 | 2e-11 | 25/46 (SW 900, RKO, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +7.3 | 3e-11 | 24/45 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +7.1 | 1e-10 | 20/43 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +6.7 | 2e-09 | 22/45 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +6.3 | 3e-08 | 24/45 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.4 | 6e-06 | 12/46 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +5.0 | 4e-05 | 13/44 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.6 | 3e-04 | 13/46 (LoVo, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +4.5 | 4e-04 | 15/46 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 6e-04 | 16/46 (LS 180, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.002 | 4/45 (LS 180, J82, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.002 | 9/41 (SNU-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.010 | 10/46 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.011 | 3/46 (LoVo, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6004.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.645×** | -11.4 | 2e-27 | 31/43 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.568×** | -9.6 | 2e-19 | 22/31 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.608×** | -8.8 | 3e-16 | 27/45 (AN3 CA, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.652×** | -7.9 | 6e-13 | 25/35 (C-33 A, A-172, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -7.7 | 2e-12 | 19/26 (HS-578T, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.674×** | -7.0 | 3e-10 | 24/41 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -6.5 | 7e-09 | 22/44 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.776×** | -4.7 | 2e-04 | 19/44 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.844× | -4.4 | 6e-04 | 18/46 (PANC-1, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.643×** | -4.2 | 0.001 | 11/45 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.841× | -3.1 | 0.11 | 13/44 (C32, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6004. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -9.0) |
| [[A-172 (line)]] | wt | 22.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.323× (z -8.9) |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.5) |
| [[AN3 CA (line)]] | alt | 35.1 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0667× (z -11.4) |
| [[J82 (line)]] | alt | 36.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 18.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 7.93 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +10.2) | [[Digitoxin (drug)]] 0.5 µM 0.136× (z -9.3) ⚠ cell-cycle shift, explains ~14% of this change |
| [[SW1417 (line)]] | alt | 9.97 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -9.9) |
| [[SW480 (line)]] | alt | 18.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -18.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -11.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 14.4 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.157× (z -9.1) |
| [[H4 (line)]] | wt | 12.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 22.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -11.7) |
| [[Hs 766T (line)]] | wt | 11.1 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.133× (z -10.4) |
| [[HS-578T (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0555× (z -19.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -9.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 22.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -8.6) |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0909× (z -8.9) |
| [[A-427 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6004), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF329]] | +0.65 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[PDRG1]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[KBTBD6]] | +0.61 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[MSL3P1]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[MAP1S]] | +0.60 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[NSUN5]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ZNF264]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MTMR9]] | +0.59 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[COMMD2]] | +0.58 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[MTRES1]] | +0.58 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[DHX57]] | +0.57 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[LRRC8E]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[XNDC1N]] | -0.57 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[PCAT1]] | -0.54 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[LARP4B]] | -0.54 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[M6PR]] | -0.53 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[CNOT1]] | -0.53 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CD164]] | -0.53 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[ATP11C]] | -0.53 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[EDEM1]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[CDIPT]] | -0.51 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[CMPK1]] | -0.50 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[NXT2]] | -0.50 | -0.24 / -0.50 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZIM2-AS1]] | B | ZIM2-AS1 activity raises PGBD1's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without ZIM2-AS1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[BRSK1]] | B | BRSK1 activity raises PGBD1's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.98× lower at baseline in the lines without BRSK1 | 0.025 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises PGBD1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF329]] | B | ZNF329 activity raises PGBD1's level | lines that do not express ZNF329 (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without ZNF329 | 0.054 | ⚠ within organs, on part of the lines; also absent: C2orf27A |
| [[APBB1]] | B | APBB1 activity raises PGBD1's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 1.84× lower at baseline in the lines without APBB1 | 0.062 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |
| [[ZFP37]] | B | ZFP37 activity raises PGBD1's level | lines that do not express ZFP37 (14) vs lines expressing it (36) | 1.90× lower at baseline in the lines without ZFP37 | 0.063 | ⚠ within organs, on part of the lines; also absent: ZNF883, HEG1, RECK |
| [[FBXO17]] | B | FBXO17 activity raises PGBD1's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 1.74× lower at baseline in the lines without FBXO17 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[ZNF569]] | B | ZNF569 activity raises PGBD1's level | lines that do not express ZNF569 (14) vs lines expressing it (36) | 1.82× lower at baseline in the lines without ZNF569 | 0.072 | ⚠ within organs, on part of the lines; also absent: ZNF570, PEG10, DNAAF9 |
| [[CERS4]] | B | CERS4 activity raises PGBD1's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 1.55× lower at baseline in the lines without CERS4 | 0.078 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.6, -1.2); signed map (-12.2, -20.7). **Vector** length 80.8, 14.6% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.0 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.8 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +5.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -11.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -8.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.9 | -7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -4.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | piggyBac transposable element derived 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:28,281,572-28,302,549 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HUCEP-4, dJ874C20.4, SCAND4 |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing; PiggyBac transposable element derived family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JS3](https://www.uniprot.org/uniprotkb/Q96JS3) (PiggyBac transposable element-derived protein 1):

> Transposase-derived from PiggyBac DNA transposons. Although it has been fully domesticated and lacks transposase activity, PGBD1 has acquired DNA-binding capability. It preferentially binds in and around genes involved in neuronal development, leading to their transcriptional pausing. Notably, PGBD1 suppresses paraspeckle assembly in neuronal cells.

**Summary**, from NCBI Gene [84547](https://www.ncbi.nlm.nih.gov/gene/84547):

> The piggyBac family of proteins, found in diverse animals, are transposases related to the transposase of the canonical piggyBac transposon from the moth, Trichoplusia ni. This family also includes genes in several genomes, including human, that appear to have been derived from the piggyBac transposons. This gene belongs to the subfamily of piggyBac transposable element derived (PGBD) genes. The PGBD proteins appear to be novel, with no obvious relationship to other transposases, or other known …

**Accessions** — [HGNC:19398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19398) · Entrez [84547](https://www.ncbi.nlm.nih.gov/gene/84547) · UniProt [Q96JS3](https://www.uniprot.org/uniprotkb/Q96JS3) · Ensembl [ENSG00000137338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137338)

## Data

Gene col 6004: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6004); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6004, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6004]; `tensor/DDL_lfc|DDL_z.npy` [6004]; `embed/gene_vectors.npy` [6004]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6004 or target_col == 6004). Every well: [[PGBD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGBD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
