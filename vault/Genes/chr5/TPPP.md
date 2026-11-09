---
symbol: "TPPP"
type: "gene"
col: 10098
ensembl_id: "ENSG00000171368"
name: "tubulin polymerization promoting protein"
location: "5p15.33"
module: 15
arm: "-"
pooled_cpm: 5.89
n_lines_expressing: 47
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TPPP

*tubulin polymerization promoting protein* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.17× (z +18.7, q 0e+00, up in 43 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.519× (z -7.4, q 6e-11, down in 22 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.546× (z -3.6, q 0.080, down in 9 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HS-578T 0.0848×, SW480 0.203×; ⚠ cell-cycle shift, would explain all of this change); [[Pitavastatin (Calcium) (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0459×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW1417 0.122×; ⚠ toxic; transcription drop); [[Sinomenine (drug)]] 0.05 µM in 1 line (SHP-77 0.0723×); [[Furosemide (drug)]] 0.5 µM in 1 line (Hs 766T 0.0739×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC11B]] (+0.81, fdr 7e-06, ⚠ same locus), [[NGFR]] (+0.64, fdr 1e-05), [[USP2]] (+0.62, fdr 1e-05), [[CYRIA]] (+0.62, fdr 1e-05); moves opposite to [[TMEM11-DT]] (-0.64, fdr 1e-05), [[METTL4]] (-0.61, fdr 2e-05), [[HSPA14]] (-0.60, fdr 3e-05).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZDHHC11B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.17×** | +18.7 | 0e+00 | 43/44 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.89×** | +18.0 | 0e+00 | 42/43 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.83×** | +16.7 | 0e+00 | 23/31 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.86×** | +15.3 | 0e+00 | 42/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.41×** | +14.1 | 3e-43 | 34/43 (SW480, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **2.88×** | +12.0 | 3e-31 | 28/44 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.69×** | +11.2 | 2e-27 | 35/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.83×** | +9.7 | 2e-20 | 19/43 (PANC-1, SW1417, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.41×** | +9.6 | 4e-20 | 24/39 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **2.32×** | +9.6 | 6e-20 | 26/40 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.12×** | +8.5 | 7e-16 | 27/41 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +6.7 | 9e-10 | 19/35 (A-172, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.00×** | +6.5 | 3e-09 | 21/39 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Simotinib (drug)]] 0.05 µM |  | **1.66×** | +5.3 | 4e-06 | 13/39 (LS 180, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.58×** | +5.2 | 6e-06 | 16/42 (PANC-1, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10098.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HS-578T 0.0848×, SW480 0.203×; ⚠ cell-cycle shift, would explain all of this change); [[Pitavastatin (Calcium) (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0459×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW1417 0.122×; ⚠ toxic; transcription drop); [[Sinomenine (drug)]] 0.05 µM in 1 line (SHP-77 0.0723×); [[Furosemide (drug)]] 0.5 µM in 1 line (Hs 766T 0.0739×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -7.4 | 6e-11 | 22/34 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.546×** | -3.6 | 0.080 | 9/35 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.732×** | -3.5 | 0.080 | 14/42 (SW1417, A549, …) | rises with dose | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **0.561×** | -3.4 | 0.087 | 9/26 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.747× | -3.3 | 0.11 | 15/44 (SW480, LoVo, …) | rises with dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.764× | -3.0 | 0.22 | 9/44 (H4, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.62 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +16.1) | — |
| [[SW1417 (line)]] | alt | 11.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -10.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 6.57 | 3 | 1 (1 ⚠) | [[Selinexor (drug)]] 0.05 µM 5.48× (z +9.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 4.61 | 2 | 0 | [[Selinexor (drug)]] 5 µM 5.32× (z +11.2) | — |
| [[A-172 (line)]] | wt | 7.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +10.7) | — |
| [[A498 (line)]] | wt | 2.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +10.4) | — |
| [[A549 (line)]] | wt | 5.99 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0895× (z -9.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.114× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 5.11 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0459× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 2.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 60.0× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 7.14 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0739× (z -9.3) |
| [[HS-578T (line)]] | alt | 5.88 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0848× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 2.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 2.91 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 16.0× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 8.32 | 0 | 1 | — | [[Sinomenine (drug)]] 0.05 µM 0.0723× (z -9.6) |
| [[A-427 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.903 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC11B]] | +0.81 | +0.76 / +0.83 | both halves | 7e-06 | ⚠ same locus (17.0 kb, same strand: neighbours can correlate without regulation) |
| [[NGFR]] | +0.64 | +0.50 / +0.76 | both halves | 1e-05 |  |
| [[USP2]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CYRIA]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[DDAH2]] | +0.60 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[NDRG4]] | +0.60 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[TUFT1]] | +0.60 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[CKB]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PPL]] | +0.59 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[KLF11]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ADGRG1]] | +0.58 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[CAPN5]] | +0.58 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[RAP1GAP]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11-DT]] | -0.64 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[METTL4]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[HSPA14]] | -0.60 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[C2orf42]] | -0.58 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[GLUD1P3]] | -0.57 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[MSANTD2]] | -0.57 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[TIMM23B-AGAP6]] | -0.57 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[AGAP5]] | -0.56 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[DNAAF10]] | -0.55 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[ZNF718]] | -0.54 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ANXA2R-OT1]] | -0.54 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[BMS1P4-1]] | -0.53 | -0.18 / -0.49 | ⚠ not reproduced | 1e-03 |  |
| [[MCM9]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZDHHC11B]] | B | ZDHHC11B activity raises TPPP's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 2.11× lower at baseline in the lines without ZDHHC11B | 0.024 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[PCDH1]] | B | PCDH1 activity raises TPPP's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.58× lower at baseline in the lines without PCDH1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[PADI2]] | B | PADI2 activity raises TPPP's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.51× lower at baseline in the lines without PADI2 | 0.072 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[DUSP15]] | B | DUSP15 activity raises TPPP's level | lines that do not express DUSP15 (15) vs lines expressing it (35) | 1.36× lower at baseline in the lines without DUSP15 | 0.084 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96 |
| [[FZD5]] | C | FZD5 activity raises TPPP's level | lines that do not express FZD5 (4) vs lines expressing it (46) | 2.02× lower at baseline in the lines without FZD5 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PCBD1, KIAA1671, TUFT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-8.2, 31.6); signed map (-1.6, 21.4). **Vector** length 77.4, 13.8% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.1 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +14.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.6 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +16.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -3.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | tubulin polymerization promoting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:659,862-693,352 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p25alpha, TPPP1, p25, TPPP/p25 |
| Gene groups (HGNC) | Tubulin polymerization promoting proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O94811](https://www.uniprot.org/uniprotkb/O94811) (Tubulin polymerization-promoting protein):

> Regulator of microtubule dynamics that plays a key role in myelination by promoting elongation of the myelin sheath. Acts as a microtubule nucleation factor in oligodendrocytes: specifically localizes to the postsynaptic Golgi apparatus region, also named Golgi outpost, and promotes microtubule nucleation, an important step for elongation of the myelin sheath. Required for both uniform polarized growth of distal microtubules as well as directing the branching of proximal processes. Shows …

**Summary**, from NCBI Gene [11076](https://www.ncbi.nlm.nih.gov/gene/11076):

> Enables several functions, including GTPase activity; magnesium ion binding activity; and protein homodimerization activity. Involved in several processes, including microtubule cytoskeleton organization; negative regulation of tubulin deacetylation; and positive regulation of protein polymerization. Located in several cellular components, including cytoskeleton; cytosol; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24164) · Entrez [11076](https://www.ncbi.nlm.nih.gov/gene/11076) · UniProt [O94811](https://www.uniprot.org/uniprotkb/O94811) · Ensembl [ENSG00000171368](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171368)

## Data

Gene col 10098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10098); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10098]; `tensor/DDL_lfc|DDL_z.npy` [10098]; `embed/gene_vectors.npy` [10098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10098 or target_col == 10098). Every well: [[TPPP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPPP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
