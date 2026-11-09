---
symbol: "SMYD2"
type: "gene"
col: 6758
ensembl_id: "ENSG00000143499"
name: "SET and MYND domain containing 2"
location: "1q32.3"
module: 105
arm: "+"
pooled_cpm: 42.7
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# SMYD2

*SET and MYND domain containing 2* — 1q32.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.239× (z -35.1, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTDSS1]] (+0.63, fdr 3e-05), [[HK1]] (+0.60, fdr 7e-06), [[LRRC20]] (+0.59, fdr 3e-05); moves opposite to [[DUSP16]] (-0.60, fdr 1e-05), [[ELF3-AS1]] (-0.59, fdr 1e-05), [[CHD2]] (-0.58, fdr 2e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 5 µM |  | 1.49× | +3.7 | 0.14 | 16/48 (C32, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 1.46× | +3.4 | 0.17 | 13/47 (HOP62, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.30 | 9/48 (SK-MEL-2, A-427, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.22× | +3.0 | 0.37 | 10/47 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.239×** | -35.1 | 0e+00 | 47/47 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.253×** | -23.9 | 0e+00 | 47/48 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.253×** | -22.9 | 0e+00 | 44/48 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.287×** | -21.6 | 0e+00 | 47/48 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.331×** | -19.1 | 0e+00 | 47/48 (SNU-423, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.349×** | -18.2 | 0e+00 | 41/47 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.554×** | -10.2 | 1e-22 | 41/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -9.9 | 2e-21 | 32/48 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.568×** | -9.8 | 8e-21 | 39/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -9.1 | 5e-18 | 39/47 (SNU-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.615×** | -8.4 | 2e-15 | 34/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -8.0 | 5e-14 | 31/47 (NCI-H23, C32, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -7.5 | 2e-12 | 33/46 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -6.8 | 4e-10 | 32/48 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.685×** | -6.6 | 2e-09 | 32/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -6.5 | 2e-09 | 34/48 (SK-MEL-2, C32, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.779×** | -6.1 | 4e-08 | 27/48 (C32, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 85.3 | 0 | 14 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -26.6) |
| [[A-172 (line)]] | wt | 41.7 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -24.6) |
| [[SK-MEL-2 (line)]] | alt | 52.1 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -30.8) |
| [[NCI-H23 (line)]] | alt | 36.9 | 0 | 10 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0672× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 57.8 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -28.4) |
| [[MIA PaCa-2 (line)]] | alt | 57.6 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -20.2) |
| [[NCI-H1573 (line)]] | alt | 38.9 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0891× (z -30.2) |
| [[SNU-1 (line)]] | wt | 66.2 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0968× (z -21.6) |
| [[A498 (line)]] | wt | 34.9 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -18.2) |
| [[HEC-1-A (line)]] | alt | 66.0 | 0 | 8 | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -21.6) |
| [[J82 (line)]] | alt | 49.5 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -23.4) |
| [[NCI-H460 (line)]] | wt | 49.8 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -29.1) |
| [[Panc 03.27 (line)]] | alt | 49.4 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -14.3) |
| [[A549 (line)]] | wt | 34.8 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -17.4) |
| [[HOP62 (line)]] | alt | 66.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -24.4) |
| [[HS-578T (line)]] | alt | 35.1 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -21.5) |
| [[PANC-1 (line)]] | alt | 29.3 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -22.6) |
| [[SW480 (line)]] | alt | 56.9 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -19.2) |
| [[AsPC-1 (line)]] | alt | 32.1 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -17.7) |
| [[Hs 766T (line)]] | wt | 31.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -15.4) |
| [[LS 180 (line)]] | wt | 59.9 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -19.1) |
| [[SNU-423 (line)]] | alt | 39.3 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.107× (z -17.3) |
| [[CFPAC-1 (line)]] | alt | 42.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -19.2) |
| [[HCT15 (line)]] | alt | 78.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -20.4) |
| [[NCI-H1792 (line)]] | alt | 31.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -16.2) |
| [[NCI-H2347 (line)]] | alt | 40.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -20.6) |
| [[RKO (line)]] | wt | 32.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -16.2) |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.151× (z -12.6) |
| [[H4 (line)]] | wt | 53.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 32.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -11.3) |
| [[LoVo (line)]] | wt | 31.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 34.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -20.8) |
| [[SW48 (line)]] | wt | 44.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -13.3) |
| [[BT-474 (line)]] | alt | 23.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 56.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.3) |
| [[KATO III (line)]] | alt | 21.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 42.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.2) |
| [[SHP-77 (line)]] | alt | 57.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -14.7) |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 2 | — | [[Pemetrexed (drug)]] 5 µM 0.0863× (z -9.7) |
| [[HT-29 (line)]] | alt | 23.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -12.3) |
| [[SW 900 (line)]] | alt | 33.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -10.8) |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -9.8) |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0984× (z -12.3) |
| [[A-427 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTDSS1]] | +0.63 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[HK1]] | +0.60 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[LRRC20]] | +0.59 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[SRD5A1]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ANKRD36B]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[POLR3G]] | +0.57 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[PYGL]] | +0.57 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[MAP2K1]] | +0.56 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[SFXN1]] | +0.56 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[IMPDH1]] | +0.55 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[CHSY1]] | +0.55 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[SLC25A15]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP16]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ELF3-AS1]] | -0.59 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[CHD2]] | -0.58 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[ANKHD1]] | -0.56 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[MVP-DT]] | -0.56 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[RBM47]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ELF3]] | -0.52 | -0.31 / -0.65 | both halves | 2e-04 |  |
| [[CTNND1]] | -0.51 | -0.22 / -0.57 | both halves | 6e-04 |  |
| [[MUC20]] | -0.51 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[CASC9]] | -0.51 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[PDZK1IP1]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[KRTAP5-AS1]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SMYD2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ODF3B]] | B | ODF3B activity lowers SMYD2's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.26× higher at baseline in the lines without ODF3B | 0.084 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.475). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.7, -10.2); signed map (-43.2, 23.7). **Vector** length 79.8, 20.6% of its response variance represented; |z| ≥ 3 in 1,352 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | -9.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.2 | +3.0 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -22.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.8 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | SET and MYND domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:214,281,102-214,337,131 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSKM-B, ZMYND14, KMT3C |
| Gene groups (HGNC) | Zinc fingers MYND-type; SET domain containing; Non-histone lysine methyltransferases |
| Reactome | 6 pathways, smallest: Regulation of TP53 Activity through Methylation; PKMTs methylate histone lysines; Regulation of TP53 Activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRG4](https://www.uniprot.org/uniprotkb/Q9NRG4) (N-lysine methyltransferase SMYD2):

> Protein-lysine N-methyltransferase that methylates both histones and non-histone proteins, including p53/TP53 and RB1. Specifically trimethylates histone H3 'Lys-4' (H3K4me3) in vivo. The activity requires interaction with HSP90alpha. Shows even higher methyltransferase activity on p53/TP53. Monomethylates 'Lys-370' of p53/TP53, leading to decreased DNA-binding activity and subsequent transcriptional regulation activity of p53/TP53. Monomethylates RB1 at 'Lys-860'.

**Summary**, from NCBI Gene [56950](https://www.ncbi.nlm.nih.gov/gene/56950):

> SET domain-containing proteins, such as SMYD2, catalyze lysine methylation (Brown et al., 2006 [PubMed 16805913]).[supplied by OMIM, Nov 2008]

**Accessions** — [HGNC:20982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20982) · Entrez [56950](https://www.ncbi.nlm.nih.gov/gene/56950) · UniProt [Q9NRG4](https://www.uniprot.org/uniprotkb/Q9NRG4) · Ensembl [ENSG00000143499](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143499)

## Data

Gene col 6758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6758); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6758]; `tensor/DDL_lfc|DDL_z.npy` [6758]; `embed/gene_vectors.npy` [6758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6758 or target_col == 6758). Every well: [[SMYD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMYD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
