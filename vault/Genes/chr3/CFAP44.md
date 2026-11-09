---
symbol: "CFAP44"
type: "gene"
col: 13046
ensembl_id: "ENSG00000206530"
name: "cilia and flagella associated protein 44"
location: "3q13.2"
module: 221
arm: "+"
pooled_cpm: 52.45
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/221"]
generated_by: "tahoemap"
---

# CFAP44

*cilia and flagella associated protein 44* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +4.5, q 0.002, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.233× (z -12.7, q 6e-34, down in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.280× (z -11.1, q 5e-26, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC11]] (+0.58, fdr 1e-05), [[KANSL1L-AS1]] (+0.57, fdr 1e-05), [[APPAT]] (+0.55, fdr 1e-05); moves opposite to [[IAH1]] (-0.58, fdr 1e-05), [[STPG1]] (-0.54, fdr 4e-05), [[SLC35A1]] (-0.54, fdr 3e-05).
> It is in [[Module 221]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13046.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.5 | 0.002 | 29/45 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.5 | 0.002 | 27/46 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.3 | 0.003 | 32/46 (SW1417, A549, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.012 | 32/46 (NCI-H460, SW480, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.56×** | +3.9 | 0.012 | 31/46 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.59×** | +3.3 | 0.082 | 25/46 (H4, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.085 | 27/45 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.43× | +3.1 | 0.12 | 25/46 (SW1417, HepG2/C3A, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.42× | +3.1 | 0.14 | 22/46 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | 1.41× | +3.0 | 0.15 | 22/46 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13046.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.233×** | -12.7 | 6e-34 | 44/45 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.280×** | -11.1 | 5e-26 | 42/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.312×** | -10.1 | 7e-22 | 39/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.366×** | -8.7 | 4e-16 | 39/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.401×** | -7.9 | 2e-13 | 40/46 (HT-29, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.562×** | -7.1 | 1e-10 | 33/46 (SW 900, HepG2/C3A, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.442×** | -6.8 | 7e-10 | 32/45 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.514×** | -5.8 | 5e-07 | 28/46 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.528×** | -5.4 | 5e-06 | 38/46 (SHP-77, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.539×** | -5.4 | 5e-06 | 35/46 (KATO III, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.523×** | -5.3 | 5e-06 | 35/46 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.362×** | -4.6 | 2e-04 | 33/45 (SNU-1, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.364×** | -4.6 | 2e-04 | 32/47 (KATO III, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.604×** | -4.2 | 1e-03 | 30/45 (SNU-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.405×** | -4.1 | 0.002 | 24/35 (NCI-H1792, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.732×** | -3.8 | 0.005 | 26/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.648×** | -3.1 | 0.060 | 24/46 (Panc 03.27, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.702×** | -3.1 | 0.060 | 22/46 (CFPAC-1, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13046. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 133 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -15.0) |
| [[KATO III (line)]] | alt | 91.4 | 0 | 9 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 54.4 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.206× (z -10.4) |
| [[C32 (line)]] | wt | 72.4 | 0 | 8 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0950× (z -11.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -10.5) |
| [[SW480 (line)]] | alt | 61.9 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 63.9 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.130× (z -12.9) |
| [[J82 (line)]] | alt | 73.0 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -11.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 91.5 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.157× (z -13.0) |
| [[BT-474 (line)]] | alt | 71.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.135× (z -12.0) |
| [[COLO 205 (line)]] | alt | 150 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.178× (z -13.0) ⚠ toxic |
| [[H4 (line)]] | wt | 64.5 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0777× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 42.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -11.9) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 48.6 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0739× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -9.2) |
| [[SNU-1 (line)]] | wt | 72.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0418× (z -17.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0964× (z -12.7) |
| [[SNU-423 (line)]] | alt | 66.2 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0812× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -10.6) |
| [[A549 (line)]] | wt | 29.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.195× (z -9.2) |
| [[HCT15 (line)]] | alt | 94.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.211× (z -9.4) |
| [[LS 180 (line)]] | wt | 75.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.213× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 43.7 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.173× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 79.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -10.4) |
| [[LoVo (line)]] | wt | 95.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.238× (z -11.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 55.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.5) ⚠ cell-cycle shift, explains ~74% of this change |
| [[A-427 (line)]] | wt | 47.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -8.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.0) ⚠ cell-cycle shift, explains ~74% of this change |
| [[MIA PaCa-2 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -10.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 31.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -8.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.110× (z -11.3) ⚠ toxic |
| [[SW48 (line)]] | wt | 40.5 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0998× (z -10.4) |
| [[A-172 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13046), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC11]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[KANSL1L-AS1]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[APPAT]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[PDC-AS1]] | +0.54 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[ALDH8A1]] | +0.54 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[LINC02798]] | +0.53 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PRH1]] | +0.53 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ALMS1]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[CD226]] | +0.51 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[HCG18]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[LINC01191]] | +0.51 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[LRGUK]] | +0.51 | +0.59 / +0.41 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IAH1]] | -0.58 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[STPG1]] | -0.54 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[SLC35A1]] | -0.54 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[EML2]] | -0.53 | -0.57 / -0.40 | both halves | 4e-05 | same gene group |
| [[BCAS4]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[CRLF3]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[CCDC88B]] | -0.50 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[NDFIP1]] | -0.50 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ACTR10]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[XKR8]] | -0.50 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[WDR41]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 | same gene group |
| [[ECHDC3]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CFAP44's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[APPAT]] | B | APPAT activity raises CFAP44's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without APPAT | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[APPAT]] | B | APPAT activity strengthens CFAP44's drug response | lines that do not express APPAT (6) vs lines expressing it (40) | the lines without APPAT respond 0.54× as strongly (z diff +2.36); strongest at Niclosamide (olamine) 5 µM: 0.95x vs 0.38x (z diff +4.6) | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers CFAP44's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 221]]; 10 genes; every member is in the + arm (projection on the module's main direction -0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.1, -10.2); signed map (15.5, 1.6). **Vector** length 98.3, 33.1% of its response variance represented; |z| ≥ 3 in 1,203 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | -4.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | -0.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.3 | +0.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.7 | -2.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.2 | -4.2 |
|  | [[Neratinib (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:113,286,930-113,441,610 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11142; previously WDR52 |
| Gene groups (HGNC) | WD repeat domain containing; Cilia and flagella associated; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MT7](https://www.uniprot.org/uniprotkb/Q96MT7) (Cilia- and flagella-associated protein 44):

> Flagellar protein involved in sperm flagellum axoneme organization and function.

**Summary**, from NCBI Gene [55779](https://www.ncbi.nlm.nih.gov/gene/55779):

> Enables peptidase activity. Involved in sperm axoneme assembly. Acts upstream of or within microtubule cytoskeleton organization. Predicted to be located in cytoskeleton and motile cilium. Predicted to be active in axoneme. Implicated in spermatogenic failure 20. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25631) · Entrez [55779](https://www.ncbi.nlm.nih.gov/gene/55779) · UniProt [Q96MT7](https://www.uniprot.org/uniprotkb/Q96MT7) · Ensembl [ENSG00000206530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206530)

## Data

Gene col 13046: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13046); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13046, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13046]; `tensor/DDL_lfc|DDL_z.npy` [13046]; `embed/gene_vectors.npy` [13046]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13046 or target_col == 13046). Every well: [[CFAP44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
