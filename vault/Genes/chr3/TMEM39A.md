---
symbol: "TMEM39A"
type: "gene"
col: 10686
ensembl_id: "ENSG00000176142"
name: "transmembrane protein 39A"
location: "3q13.33"
module: 56
arm: "+"
pooled_cpm: 130.89
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 28
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TMEM39A

*transmembrane protein 39A* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.59× (z +5.3, q 8e-05, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.245× (z -14.2, q 3e-43, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.558× (z -8.2, q 3e-14, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPA]] (+0.85, fdr 7e-06), [[PRRC1]] (+0.85, fdr 7e-06), [[COG6]] (+0.84, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[YIPF2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +5.3 | 8e-05 | 46/49 (HS-578T, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.36×** | +4.7 | 6e-04 | 40/48 (hTERT-HPNE, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.34 | 31/48 (HT-29, NCI-H1573, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10686.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.245×** | -14.2 | 3e-43 | 43/44 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.289×** | -13.1 | 2e-36 | 48/49 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.558×** | -8.2 | 3e-14 | 43/49 (A498, H4, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.444×** | -8.2 | 3e-14 | 47/48 (NCI-H2347, SW 1088, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.478×** | -7.8 | 9e-13 | 41/48 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.452×** | -7.7 | 1e-12 | 37/45 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.481×** | -7.7 | 1e-12 | 40/48 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.513×** | -7.0 | 2e-10 | 44/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.547×** | -6.3 | 2e-08 | 36/48 (A498, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.644×** | -6.1 | 5e-08 | 32/48 (NCI-H1792, NCI-H2347, …) | all doses, flat | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.666×** | -5.8 | 4e-07 | 45/48 (HS-578T, HOP62, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.586×** | -5.6 | 1e-06 | 39/48 (C32, A549, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -5.5 | 2e-06 | 31/48 (NCI-H2347, SW 900, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.630×** | -4.7 | 1e-04 | 35/48 (J82, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.649×** | -4.4 | 5e-04 | 32/50 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.664×** | -4.3 | 6e-04 | 32/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.755×** | -4.0 | 0.002 | 33/48 (RPMI-7951, NCI-H460, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.690×** | -3.9 | 0.003 | 35/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.698×** | -3.8 | 0.005 | 33/48 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.733×** | -3.2 | 0.030 | 29/48 (CFPAC-1, H4, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.751×** | -3.0 | 0.059 | 27/49 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.756×** | -2.9 | 0.072 | 24/48 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.761×** | -2.9 | 0.088 | 27/48 (RKO, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 159 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.317× (z -11.1) |
| [[A498 (line)]] | wt | 176 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 227 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.211× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 142 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -13.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.318× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 156 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.253× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 219 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -12.5) |
| [[A-172 (line)]] | wt | 119 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 150 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.401× (z -8.6) |
| [[H4 (line)]] | wt | 289 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0890× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -12.6) |
| [[HS-578T (line)]] | alt | 225 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -9.7) |
| [[A549 (line)]] | wt | 125 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0655× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.250× (z -10.9) |
| [[SW 900 (line)]] | alt | 154 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -13.2) |
| [[SW1417 (line)]] | alt | 174 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.304× (z -9.4) |
| [[HT-29 (line)]] | alt | 129 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -11.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 145 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -8.5) |
| [[CHP-212 (line)]] | wt | 125 | 0 | 3 (2 ⚠) | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.159× (z -11.0) |
| [[KATO III (line)]] | alt | 130 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -13.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 126 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 123 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -17.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.337× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 112 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0874× (z -16.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 120 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -15.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 88.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 1088 (line)]] | alt | 201 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -11.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0840× (z -10.2) |
| [[C32 (line)]] | wt | 88.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.215× (z -9.4) |
| [[HCT15 (line)]] | alt | 181 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -13.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 166 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -9.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -10.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 93.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[IQ 1 (drug)]] 5 µM 0.125× (z -8.7) |
| [[SW480 (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 96.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 169 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0509× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 1271 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0708× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 96.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 83.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 99.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPA]] | +0.85 | +0.89 / +0.82 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.85 | +0.92 / +0.82 | both halves | 7e-06 |  |
| [[COG6]] | +0.84 | +0.89 / +0.78 | both halves | 7e-06 |  |
| [[GORASP2]] | +0.84 | +0.89 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[SEC23A]] | +0.84 | +0.86 / +0.81 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.84 | +0.87 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[NUS1]] | +0.83 | +0.86 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[OSTC]] | +0.82 | +0.83 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[SEC13]] | +0.82 | +0.85 / +0.80 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.81 | +0.84 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[YIPF2]] | +0.80 | +0.86 / +0.72 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.80 | +0.84 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TMEM39A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SNHG18]] | B | SNHG18 activity raises TMEM39A's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.32× lower at baseline in the lines without SNHG18 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YIPF2]] | C | TMEM39A's natural level strengthens YIPF2's drug response | TMEM39A's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.57; direction not clear | 0.033 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[COPB1]] | C | TMEM39A's natural level strengthens COPB1's drug response | TMEM39A's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.23; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.861). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.6, -32.9); signed map (-50.9, 9.9). **Vector** length 112, 47.7% of its response variance represented; |z| ≥ 3 in 1,175 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.71 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.72 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.72 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.3 | -7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.5 | -13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | -14.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.6 | +0.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.5 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | -0.1 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.4 | +0.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.7 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 39A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:119,428,949-119,468,830 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10902, SUSR2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NV64](https://www.uniprot.org/uniprotkb/Q9NV64) (Transmembrane protein 39A):

> Regulates autophagy by controlling the spatial distribution and levels of the intracellular phosphatidylinositol 4-phosphate (PtdIns(4)P) pools. Modulates (PtdIns(4)P) levels by regulating the ER-to-Golgi trafficking of the phosphatidylinositide phosphatase SACM1L.; (Microbial infection) Positively regulates the replication of encephalomyocarditis virus (EMCV) via autophagy-dependent pathway.

**Summary**, from NCBI Gene [55254](https://www.ncbi.nlm.nih.gov/gene/55254):

> Involved in negative regulation of autophagosome assembly; negative regulation of autophagosome maturation; and positive regulation of viral genome replication. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25600) · Entrez [55254](https://www.ncbi.nlm.nih.gov/gene/55254) · UniProt [Q9NV64](https://www.uniprot.org/uniprotkb/Q9NV64) · Ensembl [ENSG00000176142](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176142)

## Data

Gene col 10686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10686); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10686]; `tensor/DDL_lfc|DDL_z.npy` [10686]; `embed/gene_vectors.npy` [10686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10686 or target_col == 10686). Every well: [[TMEM39A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM39A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
