---
symbol: "MCEE"
type: "gene"
col: 4523
ensembl_id: "ENSG00000124370"
name: "methylmalonyl-CoA epimerase"
location: "2p13.3"
module: 56
arm: "+"
pooled_cpm: 33.68
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 41
n_dd_up_clean: 5
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# MCEE

*methylmalonyl-CoA epimerase* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 0.5 µM: 1.35× (z +4.0, q 0.037, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.327× (z -21.0, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG3]] (+0.77, fdr 7e-06), [[KDELR2]] (+0.77, fdr 7e-06), [[COG6]] (+0.77, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HM13]] → it (grade C ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4523.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.037 | 22/48 (SNU-423, Panc 03.27, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.045 | 17/48 (SW1417, AsPC-1, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.045 | 15/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.045 | 16/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Trimetrexate (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.056 | 16/48 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | 1.28× | +3.2 | 0.11 | 14/48 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | position effect removed |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.5 µM |  | 1.26× | +3.1 | 0.11 | 13/48 (NCI-H2347, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.11 | 13/48 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 5 µM |  | 1.26× | +3.1 | 0.11 | 10/48 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4523.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.327×** | -21.0 | 0e+00 | 41/47 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.321×** | -14.5 | 1e-45 | 40/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.393×** | -12.4 | 3e-33 | 35/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.397×** | -12.3 | 1e-32 | 40/47 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.404×** | -12.1 | 2e-31 | 33/47 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.408×** | -11.9 | 7e-31 | 41/48 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.418×** | -11.6 | 3e-29 | 43/48 (HS-578T, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.419×** | -11.1 | 6e-27 | 25/35 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.452×** | -10.5 | 3e-24 | 37/48 (NCI-H460, KATO III, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.457×** | -10.4 | 1e-23 | 39/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.531×** | -8.4 | 2e-15 | 33/48 (H4, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.523×** | -8.3 | 5e-15 | 31/45 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.573×** | -7.4 | 7e-12 | 34/44 (KATO III, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.560×** | -7.3 | 1e-11 | 32/48 (HT-29, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.565×** | -7.0 | 9e-11 | 26/38 (A-172, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.711×** | -6.4 | 7e-09 | 31/48 (hTERT-HPNE, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.629×** | -5.9 | 1e-07 | 28/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.632×** | -5.6 | 6e-07 | 27/46 (A549, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.765×** | -5.0 | 2e-05 | 27/48 (hTERT-HPNE, Hs 766T, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.713×** | -4.5 | 2e-04 | 22/48 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.721×** | -4.3 | 4e-04 | 23/48 (LS 180, NCI-H1792, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.728×** | -4.2 | 6e-04 | 22/48 (A-172, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4523. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 57.6 | 0 | 12 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0442× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.122× (z -19.5) |
| [[HOP62 (line)]] | alt | 45.0 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -22.3) |
| [[NCI-H460 (line)]] | wt | 28.3 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -17.2) |
| [[HS-578T (line)]] | alt | 58.5 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -25.3) |
| [[SW480 (line)]] | alt | 41.3 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0472× (z -23.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.271× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 57.1 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -19.7) |
| [[SW 900 (line)]] | alt | 45.0 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -20.6) |
| [[A498 (line)]] | wt | 70.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -23.0) |
| [[A549 (line)]] | wt | 36.4 | 0 | 8 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.110× (z -16.8) |
| [[KATO III (line)]] | alt | 69.8 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.417× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 43.0 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.301× (z -12.3) |
| [[H4 (line)]] | wt | 61.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.8) |
| [[HT-29 (line)]] | alt | 37.8 | 0 | 7 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.182× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 54.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -21.8) |
| [[PANC-1 (line)]] | alt | 19.6 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.184× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 25.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -18.6) |
| [[LoVo (line)]] | wt | 41.7 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -10.1) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.210× (z -9.5) |
| [[Hs 766T (line)]] | wt | 52.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -15.9) |
| [[NCI-H2030 (line)]] | alt | 21.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 23.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -12.5) |
| [[SNU-423 (line)]] | alt | 22.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -11.5) |
| [[A-172 (line)]] | wt | 24.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 25.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -9.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.8) |
| [[SW 1088 (line)]] | alt | 76.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0321× (z -10.5) |
| [[A-427 (line)]] | wt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.6) |
| [[C32 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0832× (z -11.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -12.7) |
| [[HCT15 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.143× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.5) |
| [[SNU-1 (line)]] | wt | 36.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.113× (z -11.5) |
| [[SW1417 (line)]] | alt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.7) |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4523), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG3]] | +0.77 | +0.74 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[KDELR2]] | +0.77 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[COG6]] | +0.77 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[SRP54]] | +0.76 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.76 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[ERLEC1]] | +0.75 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.74 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[OSBP]] | +0.74 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[OSTC]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[MON2]] | +0.74 | +0.80 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HM13]] | C | HM13's natural level strengthens MCEE's drug response | HM13's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.41; direction not clear | 0.058 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | MCEE's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | MCEE's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.60 | 0.465 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, -34.7); signed map (-51.3, 11.6). **Vector** length 123, 40.6% of its response variance represented; |z| ≥ 3 in 1,387 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.61 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.62 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.62 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.7 | -3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.7 | +1.5 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.1 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -10.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.6 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.5 | -11.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -12.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.4 | -5.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -4.4 | -4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | methylmalonyl-CoA epimerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:71,109,684-71,130,239 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GLOD2, MCE, MMCE |
| Gene groups (HGNC) | Glyoxalase domain containing |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 4 pathways, smallest: Propionyl-CoA catabolism; Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PE7](https://www.uniprot.org/uniprotkb/Q96PE7) (Methylmalonyl-CoA epimerase, mitochondrial):

> Methylmalonyl-CoA epimerase involved in propionyl-CoA metabolism.

**Summary**, from NCBI Gene [84693](https://www.ncbi.nlm.nih.gov/gene/84693):

> The product of this gene catalyzes the interconversion of D- and L-methylmalonyl-CoA during the degradation of branched chain amino acids. odd chain-length fatty acids, and other metabolites. Mutations in this gene result in methylmalonyl-CoA epimerase deficiency, which is presented as mild to moderate methylmalonic aciduria. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16732](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16732) · Entrez [84693](https://www.ncbi.nlm.nih.gov/gene/84693) · UniProt [Q96PE7](https://www.uniprot.org/uniprotkb/Q96PE7) · Ensembl [ENSG00000124370](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124370)

## Data

Gene col 4523: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4523); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4523, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4523]; `tensor/DDL_lfc|DDL_z.npy` [4523]; `embed/gene_vectors.npy` [4523]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4523 or target_col == 4523). Every well: [[MCEE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCEE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
