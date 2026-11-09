---
symbol: "DHX37"
type: "gene"
col: 7472
ensembl_id: "ENSG00000150990"
name: "DEAH-box helicase 37"
location: "12q24.31"
module: 5
arm: "+"
pooled_cpm: 22.18
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 7
n_dd_up_clean: 30
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# DHX37

*DEAH-box helicase 37* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.40× (z +15.8, q 0e+00, up in 45 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +13.1, q 1e-36, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.759× (z -7.0, q 1e-09, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP20]] (+0.83, fdr 7e-06), [[MRTO4]] (+0.81, fdr 7e-06), [[NIP7]] (+0.78, fdr 7e-06); moves opposite to [[PJA2]] (-0.75, fdr 7e-06), [[ARL3]] (-0.70, fdr 8e-06), [[FBXO33]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7472.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.40×** | +15.8 | 0e+00 | 45/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +13.1 | 1e-36 | 37/47 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +10.8 | 1e-24 | 33/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +10.3 | 1e-22 | 30/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **2.66×** | +9.3 | 2e-18 | 41/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +9.1 | 1e-17 | 27/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.42×** | +8.4 | 5e-15 | 37/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +7.7 | 1e-12 | 29/45 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-733 (drug)]] 5 µM |  | **2.23×** | +7.6 | 2e-12 | 34/46 (A498, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.3 | 2e-11 | 27/48 (Hs 766T, NCI-H2347, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.16×** | +7.3 | 2e-11 | 30/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +6.8 | 5e-10 | 22/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.8 | 5e-10 | 27/47 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +6.8 | 5e-10 | 25/40 (A498, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.8 | 5e-10 | 22/45 (RPMI-7951, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 2e-08 | 24/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +6.2 | 2e-08 | 25/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.9 | 8e-08 | 22/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +5.9 | 9e-08 | 23/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7472.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.759×** | -7.0 | 1e-09 | 26/48 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.696×** | -6.6 | 2e-08 | 27/48 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.513×** | -6.3 | 5e-08 | 26/48 (PANC-1, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.711×** | -6.2 | 1e-07 | 26/47 (CHP-212, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.847× | -4.2 | 0.003 | 13/48 (RKO, HCT15, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.811×** | -3.6 | 0.027 | 18/47 (H4, J82, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | **0.823×** | -3.4 | 0.056 | 14/47 (J82, NCI-H1792, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.830×** | -3.4 | 0.056 | 11/47 (RKO, SW480, …) | top dose only |  |
| [[Rifaximin (drug)]] 0.5 µM |  | 0.843× | -3.1 | 0.13 | 9/47 (PANC-1, NCI-H661, …) | rises with dose |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.844× | -3.1 | 0.13 | 11/47 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.846× | -3.0 | 0.13 | 10/47 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 37.7 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.6) | [[Belinostat (drug)]] 5 µM 0.425× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 25.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -13.9) |
| [[A498 (line)]] | wt | 16.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 24.5 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.38× (z +10.8) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.1) | — |
| [[RKO (line)]] | wt | 39.8 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.185× (z -11.7) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 35.3 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.104× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 14.1 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.97× (z +8.6) ⚠ unreliable plate only | — |
| [[BT-474 (line)]] | alt | 23.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.0 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.44× (z +9.4) ⚠ unreliable plate only | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 14.8 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.66× (z +8.7) ⚠ unreliable plate only | — |
| [[SW48 (line)]] | wt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -8.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 31.0 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.57× (z +9.5) ⚠ unreliable plate only | — |
| [[A-172 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | +0.83 | +0.82 / +0.79 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 975 |
| [[MRTO4]] | +0.81 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[NIP7]] | +0.78 | +0.82 / +0.71 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 609 |
| [[GRWD1]] | +0.78 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[WDR4]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | STRING 477 |
| [[GPATCH4]] | +0.77 | +0.78 / +0.71 | both halves | 7e-06 | STRING 515 |
| [[PUS1]] | +0.77 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.77 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[ARMC6]] | +0.77 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[BYSL]] | +0.77 | +0.79 / +0.76 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 961 |
| [[NOP16]] | +0.76 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[TRMT1]] | +0.75 | +0.70 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJA2]] | -0.75 | -0.74 / -0.65 | both halves | 7e-06 |  |
| [[ARL3]] | -0.70 | -0.72 / -0.58 | both halves | 8e-06 |  |
| [[FBXO33]] | -0.66 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[HDAC5]] | -0.64 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.64 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.64 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[MINDY2]] | -0.64 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.64 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[CDKN2D]] | -0.63 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[CCDC28A]] | -0.63 | -0.57 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DHX37's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | DHX37's natural level raises the cells' numbers under Belzutifan 5 µM (protects the cells) | DHX37's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62 | 0.425 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.834). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.3, -35.0); signed map (-0.6, -46.1). **Vector** length 113, 28.8% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.68 to 13); *ribosome biogenesis* (control, mean cos +0.63 to 6); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.65 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +11.2 | +15.8 |
|  | [[EX229 (drug)]] 5 µM |  | +6.6 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +13.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +10.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.8 | +8.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.7 | +7.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.7 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +6.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.9 | -6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.6 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DEAH-box helicase 37 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:124,946,825-124,989,131 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1517, MGC4322, MGC2695, Dhr1; previously DDX37 |
| Gene groups (HGNC) | DEAH-box helicases; SSU processome |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY37](https://www.uniprot.org/uniprotkb/Q8IY37) (Probable ATP-dependent RNA helicase DHX37):

> ATP-binding RNA helicase that plays a role in maturation of the small ribosomal subunit in ribosome biogenesis. Required for the release of the U3 snoRNP from pre-ribosomal particles. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA …

**Summary**, from NCBI Gene [57647](https://www.ncbi.nlm.nih.gov/gene/57647):

> This gene encodes a DEAD box protein. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular …

**Accessions** — [HGNC:17210](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17210) · Entrez [57647](https://www.ncbi.nlm.nih.gov/gene/57647) · UniProt [Q8IY37](https://www.uniprot.org/uniprotkb/Q8IY37) · Ensembl [ENSG00000150990](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150990)

## Data

Gene col 7472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7472); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7472]; `tensor/DDL_lfc|DDL_z.npy` [7472]; `embed/gene_vectors.npy` [7472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7472 or target_col == 7472). Every well: [[DHX37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
