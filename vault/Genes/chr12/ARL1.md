---
symbol: "ARL1"
type: "gene"
col: 4224
ensembl_id: "ENSG00000120805"
name: "ARF like GTPase 1"
location: "12q23.2"
module: 49
arm: "+"
pooled_cpm: 56.75
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 25
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# ARL1

*ARF like GTPase 1* — 12q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.51× (z +8.6, q 4e-15, up in 35 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tofacitinib (citrate) (drug)]] 5 µM: 1.16× (z +4.0, q 0.008, up in 10 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.527× (z -13.4, q 3e-38, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RUSF1]] (+0.74, fdr 7e-06), [[MED8]] (+0.73, fdr 7e-06), [[COG6]] (+0.73, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +8.6 | 4e-15 | 35/47 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.0 | 4e-13 | 22/41 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.1 | 0.007 | 17/44 (MIA PaCa-2, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.16× | +4.0 | 0.008 | 10/49 (CFPAC-1, COLO 205, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.014 | 20/47 (SNU-1, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.21×** | +3.7 | 0.021 | 16/44 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.025 | 6/48 (HS-578T, HEC-1-A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~17% of this change | 1.18× | +3.5 | 0.028 | 20/47 (A-172, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.058 | 13/45 (PANC-1, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.073 | 11/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.073 | 13/48 (SNU-423, PANC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4224.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.527×** | -13.4 | 3e-38 | 39/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.557×** | -12.3 | 5e-32 | 38/48 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.660×** | -11.6 | 5e-29 | 34/47 (AsPC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.566×** | -11.5 | 2e-28 | 36/47 (SW 900, COLO 205, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.584×** | -11.3 | 2e-27 | 37/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.597×** | -10.8 | 3e-25 | 38/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.611×** | -10.3 | 4e-23 | 33/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -10.0 | 2e-21 | 32/48 (AsPC-1, H4, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.624×** | -9.9 | 3e-21 | 39/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -8.7 | 2e-16 | 34/48 (A498, H4, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.682×** | -8.0 | 6e-14 | 30/48 (H4, A498, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.764×** | -7.7 | 8e-13 | 31/48 (HOP62, HS-578T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.707×** | -7.0 | 1e-10 | 29/48 (SW 900, SW48, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -6.7 | 7e-10 | 30/48 (HOP62, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.559×** | -6.4 | 7e-09 | 33/49 (AsPC-1, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -6.2 | 2e-08 | 33/48 (NCI-H2347, NCI-H460, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.568×** | -6.2 | 2e-08 | 29/48 (NCI-H2347, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.736×** | -6.2 | 2e-08 | 28/48 (AsPC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.815×** | -4.0 | 0.001 | 20/47 (SW48, NCI-H2347, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.845× | -3.5 | 0.010 | 19/48 (LoVo, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 50.1 | 0 | 10 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.316× (z -13.9) |
| [[H4 (line)]] | wt | 75.4 | 0 | 9 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -13.1) |
| [[A498 (line)]] | wt | 96.8 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -12.9) |
| [[SW480 (line)]] | alt | 39.8 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 47.4 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.348× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 114 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -19.7) |
| [[HS-578T (line)]] | alt | 80.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -16.2) |
| [[SW 900 (line)]] | alt | 87.8 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.287× (z -12.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -9.6) |
| [[LoVo (line)]] | wt | 87.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -11.2) |
| [[LS 180 (line)]] | wt | 60.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.328× (z -10.5) |
| [[Hs 766T (line)]] | wt | 58.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.368× (z -9.2) |
| [[KATO III (line)]] | alt | 69.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -10.1) |
| [[COLO 205 (line)]] | alt | 41.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.153× (z -11.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 60.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -9.2) |
| [[J82 (line)]] | alt | 63.9 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 56.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.290× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 72.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -15.6) |
| [[SNU-423 (line)]] | alt | 42.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 54.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.50× (z +10.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 39.5 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0873× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 53.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -8.7) |
| [[HCT15 (line)]] | alt | 85.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.277× (z -9.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 44.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.324× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 56.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.381× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 61.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.402× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 55.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 56.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.5) |
| [[SW1417 (line)]] | alt | 55.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.439× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 49.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUSF1]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[MED8]] | +0.73 | +0.83 / +0.59 | both halves | 7e-06 |  |
| [[COG6]] | +0.73 | +0.73 / +0.64 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 786 |
| [[COPG1]] | +0.71 | +0.74 / +0.62 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[ERLEC1]] | +0.70 | +0.82 / +0.58 | both halves | 7e-06 | STRING 436 |
| [[YIPF2]] | +0.70 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[COG3]] | +0.69 | +0.74 / +0.56 | both halves | 1e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 639 |
| [[GOLGA2]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[UFL1]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.67 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[SERP1]] | +0.66 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[TBC1D23]] | +0.66 | +0.71 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARL1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.0, -33.8); signed map (-52.7, 11.3). **Vector** length 113, 33.6% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.53 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.53 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +8.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +8.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.1 | +1.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.9 | +4.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -12.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.5 | -9.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.3 | -10.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.1 | -11.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.7 | -13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -6.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.1 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.2 — chr12:101,393,116-101,407,772 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARFL1 |
| Gene groups (HGNC) | ARF GTPase family |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P40616](https://www.uniprot.org/uniprotkb/P40616) (ADP-ribosylation factor-like protein 1):

> GTP-binding protein that recruits several effectors, such as golgins, arfaptins and Arf-GEFs to the trans-Golgi network, and modulates their functions at the Golgi complex. Plays thereby a role in a wide range of fundamental cellular processes, including cell polarity, innate immunity, or protein secretion mediated by arfaptins, which were shown to play a role in maintaining insulin secretion from pancreatic beta cells.

**Summary**, from NCBI Gene [400](https://www.ncbi.nlm.nih.gov/gene/400):

> The protein encoded by this gene belongs to the ARL (ADP-ribosylation factor-like) family of proteins, which are structurally related to ADP-ribosylation factors (ARFs). ARFs, described as activators of cholera toxin (CT) ADP-ribosyltransferase activity, regulate intracellular vesicular membrane trafficking, and stimulate a phospholipase D (PLD) isoform. Although, ARL proteins were initially thought not to activate CT or PLD, later work showed that they are weak stimulators of PLD and CT in a …

**Accessions** — [HGNC:692](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:692) · Entrez [400](https://www.ncbi.nlm.nih.gov/gene/400) · UniProt [P40616](https://www.uniprot.org/uniprotkb/P40616) · Ensembl [ENSG00000120805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120805)

## Data

Gene col 4224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4224); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4224]; `tensor/DDL_lfc|DDL_z.npy` [4224]; `embed/gene_vectors.npy` [4224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4224 or target_col == 4224). Every well: [[ARL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
