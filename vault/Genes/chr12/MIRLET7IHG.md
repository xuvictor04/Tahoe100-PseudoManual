---
symbol: "MIRLET7IHG"
type: "gene"
col: 15037
ensembl_id: "ENSG00000257354"
name: "MIRLET7I host gene"
location: "12q14.1"
module: 39
arm: "+"
pooled_cpm: 38.9
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# MIRLET7IHG

*MIRLET7I host gene* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +9.7, q 1e-19, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.333× (z -11.7, q 4e-29, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM15-AS1]] (+0.80, fdr 7e-06), [[RFX3-DT]] (+0.76, fdr 1e-05), [[LINC01004]] (+0.76, fdr 7e-06); moves opposite to [[CAT]] (-0.67, fdr 7e-06), [[NDRG3]] (-0.66, fdr 3e-05), [[ARRB2]] (-0.66, fdr 5e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC26A4]] → it (grade B ⚠); 1 goes from it, the strongest it → [[REPS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15037.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +9.7 | 1e-19 | 37/47 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +5.6 | 5e-06 | 27/47 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.017 | 24/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.064 | 23/48 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | 1.36× | +3.2 | 0.18 | 21/48 (hTERT-HPNE, A-172, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.1 | 0.21 | 1/48 (RPMI-7951) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15037.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.333×** | -11.7 | 4e-29 | 42/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.380×** | -10.3 | 1e-22 | 46/48 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.384×** | -10.2 | 3e-22 | 47/48 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.445×** | -8.7 | 7e-16 | 31/47 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.439×** | -8.5 | 3e-15 | 25/35 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.461×** | -8.0 | 2e-13 | 39/47 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.448×** | -7.9 | 2e-13 | 36/48 (NCI-H1573, HepG2/C3A, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.559×** | -6.2 | 4e-08 | 39/48 (CFPAC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.354×** | -5.8 | 4e-07 | 35/49 (AsPC-1, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.359×** | -5.7 | 6e-07 | 30/47 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.594×** | -5.6 | 1e-06 | 34/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.604×** | -5.4 | 3e-06 | 38/48 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.426×** | -4.8 | 8e-05 | 33/47 (AsPC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.651×** | -4.6 | 2e-04 | 30/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.654×** | -4.5 | 2e-04 | 26/48 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.457×** | -4.4 | 4e-04 | 28/48 (AsPC-1, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.788×** | -3.6 | 0.009 | 25/48 (RKO, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.788×** | -3.6 | 0.009 | 23/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.724×** | -3.3 | 0.025 | 22/48 (A549, SW 900, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.742×** | -3.0 | 0.064 | 20/47 (C32, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.750×** | -3.0 | 0.073 | 14/48 (NCI-H2030, NCI-H460, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.7 | 0 | 14 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.341× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 72.2 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.273× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 58.6 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +12.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0528× (z -18.5) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.118× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 59.3 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0389× (z -23.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[SW480 (line)]] | alt | 25.9 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -10.9) |
| [[A549 (line)]] | wt | 40.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.226× (z -9.3) |
| [[KATO III (line)]] | alt | 29.6 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -10.9) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.204× (z -9.8) |
| [[PANC-1 (line)]] | alt | 38.0 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.168× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.314× (z -8.8) |
| [[H4 (line)]] | wt | 55.1 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.155× (z -10.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.175× (z -10.4) |
| [[LoVo (line)]] | wt | 53.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +17.2) | [[Panobinostat (drug)]] 5 µM 0.276× (z -9.4) |
| [[A-172 (line)]] | wt | 32.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 46.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.280× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 39.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.209× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.252× (z -9.2) |
| [[COLO 205 (line)]] | alt | 63.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[HEC-1-A (line)]] | alt | 55.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[HepG2_C3A (line)]] | wt | 33.4 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0590× (z -15.2) |
| [[HOP62 (line)]] | alt | 35.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -9.5) |
| [[RKO (line)]] | wt | 48.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -9.7) |
| [[SNU-423 (line)]] | alt | 42.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.122× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.202× (z -9.0) |
| [[SW48 (line)]] | wt | 14.7 | 0 | 2 | — | [[Malotilate (drug)]] 0.5 µM 0.0957× (z -8.7) |
| [[A498 (line)]] | wt | 50.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HCT15 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[J82 (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LOX-IMVI (line)]] | wt | 35.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 47.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0778× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM15-AS1]] | +0.80 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[RFX3-DT]] | +0.76 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[LINC01004]] | +0.76 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.75 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[SLC13A3]] | +0.75 | +0.78 / +0.39 | both halves | 6e-05 |  |
| [[PPP1R3F]] | +0.74 | +0.75 / +0.48 | both halves | 2e-05 |  |
| [[C3orf20]] | +0.74 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.74 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[RAB30-DT]] | +0.73 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[ANKDD1B]] | +0.73 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[TMED6]] | +0.73 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[LINC00486]] | +0.73 | +0.72 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAT]] | -0.67 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[NDRG3]] | -0.66 | -0.70 / -0.43 | both halves | 3e-05 |  |
| [[ARRB2]] | -0.66 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[UBAC1]] | -0.65 | -0.69 / -0.39 | both halves | 5e-05 |  |
| [[HACE1]] | -0.64 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[ARL6]] | -0.64 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[SMARCD3]] | -0.63 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[STX7]] | -0.63 | -0.62 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC26A4]] | B | SLC26A4 activity raises MIRLET7IHG's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.71× lower at baseline in the lines without SLC26A4 | 0.010 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[REPS1]] | C | MIRLET7IHG's natural level weakens REPS1's drug response | MIRLET7IHG's natural level across 50 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.54; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.6, -12.1); signed map (17.1, 1.4). **Vector** length 121, 38.2% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.5 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.5 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.1 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.0 | +3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +2.7 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.4 | -10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.9 | -11.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.0 | -4.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.8 | -10.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.5 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.2 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -3.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | MIRLET7I host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q14.1 — chr12:62,602,752-62,622,213 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55478) · Entrez [120766144](https://www.ncbi.nlm.nih.gov/gene/120766144) · Ensembl [ENSG00000257354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257354)

## Data

Gene col 15037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15037); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15037]; `tensor/DDL_lfc|DDL_z.npy` [15037]; `embed/gene_vectors.npy` [15037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15037 or target_col == 15037). Every well: [[MIRLET7IHG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIRLET7IHG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
