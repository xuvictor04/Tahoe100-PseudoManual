---
symbol: "NCK2"
type: "gene"
col: 973
ensembl_id: "ENSG00000071051"
name: "NCK adaptor protein 2"
location: "2q12.2"
module: 36
arm: "+"
pooled_cpm: 38.23
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# NCK2

*NCK adaptor protein 2* — 2q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.34× (z +4.6, q 0.003, up in 27 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change.
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.370× (z -23.1, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.435× (z -13.7, q 2e-40, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PACC1]] (+0.62, fdr 2e-05), [[HERC2]] (+0.62, fdr 1e-05), [[RAP1GDS1]] (+0.62, fdr 1e-05); moves opposite to [[HMGCL]] (-0.62, fdr 1e-05), [[METTL25B]] (-0.57, fdr 1e-05), [[SEC23B]] (-0.55, fdr 5e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.34×** | +4.6 | 0.003 | 27/47 (SW 900, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 973.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.370×** | -23.1 | 0e+00 | 46/48 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.418×** | -13.8 | 7e-41 | 42/48 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.435×** | -13.7 | 2e-40 | 43/48 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.494×** | -11.6 | 6e-29 | 42/48 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.528×** | -10.5 | 8e-24 | 40/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.643×** | -10.3 | 8e-23 | 36/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -8.0 | 1e-13 | 34/48 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.435×** | -7.1 | 6e-11 | 33/49 (NCI-H2030, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -7.1 | 6e-11 | 33/48 (AN3 CA, NCI-H23, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.596×** | -7.0 | 1e-10 | 30/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.655×** | -7.0 | 1e-10 | 32/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.707×** | -5.7 | 5e-07 | 29/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.719×** | -5.4 | 2e-06 | 26/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.733×** | -5.1 | 1e-05 | 24/48 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.725×** | -5.1 | 1e-05 | 27/48 (A-427, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -4.5 | 2e-04 | 23/48 (A-172, HepG2/C3A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.785×** | -4.0 | 0.002 | 22/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.802×** | -3.7 | 0.007 | 21/48 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.788×** | -3.7 | 0.007 | 16/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Silodosin (drug)]] 5 µM |  | **0.826×** | -3.0 | 0.059 | 14/47 (SW 1271, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.4 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -18.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0884× (z -32.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -19.9) |
| [[NCI-H2030 (line)]] | alt | 35.6 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -16.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -10.1) |
| [[C32 (line)]] | wt | 84.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -19.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 31.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 31.9 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -22.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -9.6) |
| [[RKO (line)]] | wt | 36.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -21.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -17.0) |
| [[SK-MEL-2 (line)]] | alt | 56.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0570× (z -34.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -12.1) |
| [[A-172 (line)]] | wt | 57.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -12.3) |
| [[A-427 (line)]] | wt | 35.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -27.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.269× (z -9.6) |
| [[HOP62 (line)]] | alt | 40.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -17.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -9.3) |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -16.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -12.1) |
| [[J82 (line)]] | alt | 32.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.8) |
| [[LoVo (line)]] | wt | 44.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -19.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 24.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -15.3) |
| [[SNU-1 (line)]] | wt | 26.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -9.0) |
| [[SW1417 (line)]] | alt | 57.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -15.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 32.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -9.0) |
| [[AN3 CA (line)]] | alt | 60.0 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -9.2) |
| [[HT-29 (line)]] | alt | 31.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -14.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 44.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -14.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -11.6) |
| [[SW480 (line)]] | alt | 36.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.458× (z -8.9) |
| [[BT-474 (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 62.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 34.5 | 0 | 1 | — | [[Trifluridine (drug)]] 0.05 µM 0.120× (z -8.5) |
| [[H4 (line)]] | wt | 54.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 54.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.439× (z -8.9) |
| [[LS 180 (line)]] | wt | 51.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 40.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -10.9) |
| [[SW48 (line)]] | wt | 40.7 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.171× (z -9.8) |
| [[A498 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | +0.62 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[HERC2]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[NIN]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[TCF3]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 | pathway: Cell-Cell communication |
| [[GNAZ]] | +0.61 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.61 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[POMT2]] | +0.61 | +0.63 / +0.57 | both halves | 9e-06 | pathway: Cell-Cell communication |
| [[ATP13A2]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[STK25]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[MAPK9]] | +0.60 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[RNF130]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGCL]] | -0.62 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[METTL25B]] | -0.57 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[SEC23B]] | -0.55 | -0.63 / -0.39 | both halves | 5e-05 |  |
| [[TRIM5]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[GALK2]] | -0.55 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[C12orf60]] | -0.54 | -0.63 / -0.34 | both halves | 1e-04 |  |
| [[SGO1-AS1]] | -0.54 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[MYNN]] | -0.54 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[SRGAP3]] | -0.53 | -0.60 / -0.40 | both halves | 5e-05 | same gene group; pathway: Signaling by ROBO receptors |
| [[HHLA3]] | -0.53 | -0.68 / -0.35 | both halves | 1e-04 |  |
| [[ZNF226]] | -0.53 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[RSPRY1]] | -0.53 | -0.59 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NCK2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-4.9, -23.2); signed map (-19.1, -50.5). **Vector** length 90.0, 22.2% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.5 | +2.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | -0.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.9 | +0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | -0.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.5 | -23.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.3 | -13.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -8.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -3.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | NCK adaptor protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.2 — chr2:105,744,912-105,894,274 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NCKbeta |
| Gene groups (HGNC) | SH2 domain containing; SH3 domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 19 pathways, smallest: Regulation of cortical dendrite branching; Activation of RAC1; Ephrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O43639](https://www.uniprot.org/uniprotkb/O43639) (Cytoplasmic protein NCK2):

> Adapter protein which associates with tyrosine-phosphorylated growth factor receptors or their cellular substrates. Maintains low levels of EIF2S1 phosphorylation by promoting its dephosphorylation by PP1. Plays a role in ELK1-dependent transcriptional activation in response to activated Ras signaling.

**Summary**, from NCBI Gene [8440](https://www.ncbi.nlm.nih.gov/gene/8440):

> This gene encodes a member of the NCK family of adaptor proteins. The protein contains three SH3 domains and one SH2 domain. The protein has no known catalytic function but has been shown to bind and recruit various proteins involved in the regulation of receptor protein tyrosine kinases. It is through these regulatory activities that this protein is believed to be involved in cytoskeletal reorganization. Alternate transcriptional splice variants, encoding different isoforms, have been …

**Accessions** — [HGNC:7665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7665) · Entrez [8440](https://www.ncbi.nlm.nih.gov/gene/8440) · UniProt [O43639](https://www.uniprot.org/uniprotkb/O43639) · Ensembl [ENSG00000071051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071051)

## Data

Gene col 973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 973); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 973]; `tensor/DDL_lfc|DDL_z.npy` [973]; `embed/gene_vectors.npy` [973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 973 or target_col == 973). Every well: [[NCK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
