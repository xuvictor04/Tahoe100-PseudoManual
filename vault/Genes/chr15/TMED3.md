---
symbol: "TMED3"
type: "gene"
col: 9330
ensembl_id: "ENSG00000166557"
name: "transmembrane p24 trafficking protein 3"
location: "15q25.1"
module: 49
arm: "+"
pooled_cpm: 85.83
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 24
n_dd_up_clean: 9
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# TMED3

*transmembrane p24 trafficking protein 3* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.45× (z +8.2, q 2e-13, up in 34 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 0.05 µM: 1.29× (z +5.3, q 4e-05, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.275× (z -39.8, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDELR2]] (+0.79, fdr 7e-06), [[CUTC]] (+0.76, fdr 7e-06), [[PDIA5]] (+0.76, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC1A1]] → it (grade B ⚠); 2 go from it, the strongest it → [[MINAR1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9330.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +8.2 | 2e-13 | 34/47 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.29×** | +5.3 | 4e-05 | 27/47 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.9 | 1e-04 | 23/47 (HT-29, LS 180, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.49×** | +4.5 | 7e-04 | 21/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +4.5 | 7e-04 | 23/47 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.003 | 18/47 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.004 | 18/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.007 | 15/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.008 | 19/47 (NCI-H1573, NCI-H1792, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.015 | 13/47 (KATO III, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.016 | 14/47 (A-172, HS-578T, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.053 | 11/47 (AsPC-1, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.053 | 17/43 (C32, C-33 A, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.087 | 11/47 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.087 | 13/47 (COLO 205, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9330.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.275×** | -39.8 | 0e+00 | 46/47 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.384×** | -20.0 | 0e+00 | 43/47 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.528×** | -19.7 | 0e+00 | 42/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.482×** | -15.7 | 0e+00 | 43/47 (A498, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.527×** | -14.0 | 3e-42 | 42/47 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.560×** | -12.6 | 1e-34 | 36/47 (KATO III, H4, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.599×** | -11.2 | 4e-27 | 34/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.451×** | -9.1 | 7e-18 | 43/48 (HS-578T, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -8.8 | 8e-17 | 34/47 (hTERT-HPNE, J82, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.678×** | -8.5 | 1e-15 | 34/47 (A498, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -7.5 | 4e-12 | 27/47 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.720×** | -7.1 | 4e-11 | 32/47 (SW48, SNU-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.734×** | -6.7 | 7e-10 | 31/47 (H4, HS-578T, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.804×** | -6.7 | 7e-10 | 28/47 (J82, Hs 766T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.754×** | -6.2 | 3e-08 | 28/47 (A498, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.759×** | -6.0 | 6e-08 | 25/47 (KATO III, H4, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.762×** | -5.5 | 1e-06 | 22/46 (A-172, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.819×** | -4.2 | 8e-04 | 18/47 (NCI-H2030, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 214 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -26.5) |
| [[A498 (line)]] | wt | 169 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -43.7) |
| [[KATO III (line)]] | alt | 146 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -23.0) |
| [[RKO (line)]] | wt | 123 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -27.5) |
| [[HOP62 (line)]] | alt | 97.8 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -30.7) |
| [[LoVo (line)]] | wt | 225 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -20.1) |
| [[BT-474 (line)]] | alt | 81.5 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -22.2) |
| [[hTERT-HPNE (line)]] | wt | 139 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -16.6) |
| [[RPMI-7951 (line)]] | alt | 150 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -27.3) |
| [[SW 900 (line)]] | alt | 97.4 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -24.3) |
| [[HS-578T (line)]] | alt | 112 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -26.4) |
| [[J82 (line)]] | alt | 95.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -29.7) |
| [[SW48 (line)]] | wt | 157 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -16.3) |
| [[NCI-H1573 (line)]] | alt | 111 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -21.6) |
| [[SW1417 (line)]] | alt | 73.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -23.4) |
| [[A-172 (line)]] | wt | 69.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -16.6) |
| [[A549 (line)]] | wt | 106 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -24.8) |
| [[AsPC-1 (line)]] | alt | 65.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -30.6) |
| [[LS 180 (line)]] | wt | 77.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -16.5) |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -31.8) |
| [[NCI-H23 (line)]] | alt | 81.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -22.3) |
| [[NCI-H460 (line)]] | wt | 66.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -23.5) |
| [[SNU-1 (line)]] | wt | 96.5 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.102× (z -18.8) ⚠ toxic; cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.140× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 72.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 49.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -19.4) |
| [[HepG2_C3A (line)]] | wt | 42.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.4) |
| [[Hs 766T (line)]] | wt | 66.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -17.1) |
| [[LOX-IMVI (line)]] | wt | 60.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 98.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 70.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -17.5) |
| [[PANC-1 (line)]] | alt | 64.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -19.1) |
| [[A-427 (line)]] | wt | 45.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -17.6) |
| [[C32 (line)]] | wt | 62.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.3) |
| [[CHP-212 (line)]] | wt | 48.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.125× (z -9.0) |
| [[COLO 205 (line)]] | alt | 80.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -14.9) |
| [[HCT15 (line)]] | alt | 81.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.305× (z -9.1) |
| [[HT-29 (line)]] | alt | 76.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -18.7) |
| [[MIA PaCa-2 (line)]] | alt | 44.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.0) |
| [[NCI-H661 (line)]] | alt | 48.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 50.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 55.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -11.6) |
| [[SNU-423 (line)]] | alt | 42.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -8.9) |
| [[AN3 CA (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.54 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDELR2]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 612 |
| [[CUTC]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[PDIA5]] | +0.76 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[SEC13]] | +0.75 | +0.72 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PMM2]] | +0.74 | +0.75 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[FAM98A]] | +0.73 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[COG3]] | +0.73 | +0.68 / +0.72 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDXDC1]] | +0.73 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[HM13]] | +0.72 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[MINAR1]] | +0.71 | +0.65 / +0.78 | both halves | 7e-06 | ⚠ **readthrough risk**: MINAR1 lies 4.9 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[SEC24D]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SND1]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[COG6]] | +0.70 | +0.70 / +0.64 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC1A1]] | B | SLC1A1 activity raises TMED3's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.95× lower at baseline in the lines without SLC1A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises TMED3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MINAR1]] | C | TMED3's natural level strengthens MINAR1's drug response | TMED3's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.59; direction not clear | 0.037 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | TMED3's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | TMED3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.486 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.3, -33.0); signed map (-50.9, 7.6). **Vector** length 131, 43.2% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.50 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.50 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.0 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.0 | +4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.5 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.7 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +4.7 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.5 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.7 | -6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -11.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.1 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -19.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -7.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane p24 trafficking protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:79,311,112-79,427,432 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p24B, p24gamma4, p24g4; previously C15orf22 |
| Gene groups (HGNC) | Transmembrane p24 trafficking proteins |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3Q3](https://www.uniprot.org/uniprotkb/Q9Y3Q3) (Transmembrane emp24 domain-containing protein 3):

> Potential role in vesicular protein trafficking, mainly in the early secretory pathway. Contributes to the coupled localization of TMED2 and TMED10 in the cis-Golgi network.

**Summary**, from NCBI Gene [23423](https://www.ncbi.nlm.nih.gov/gene/23423):

> Predicted to be involved in Golgi organization; endoplasmic reticulum to Golgi vesicle-mediated transport; and intracellular protein transport. Located in Golgi apparatus; endoplasmic reticulum; and endoplasmic reticulum-Golgi intermediate compartment. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28889](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28889) · Entrez [23423](https://www.ncbi.nlm.nih.gov/gene/23423) · UniProt [Q9Y3Q3](https://www.uniprot.org/uniprotkb/Q9Y3Q3) · Ensembl [ENSG00000166557](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166557)

## Data

Gene col 9330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9330); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9330]; `tensor/DDL_lfc|DDL_z.npy` [9330]; `embed/gene_vectors.npy` [9330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9330 or target_col == 9330). Every well: [[TMED3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMED3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
