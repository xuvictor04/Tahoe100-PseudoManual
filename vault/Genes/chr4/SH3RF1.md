---
symbol: "SH3RF1"
type: "gene"
col: 7806
ensembl_id: "ENSG00000154447"
name: "SH3 domain containing ring finger 1"
location: "4q32.3-q33"
module: 120
arm: "+"
pooled_cpm: 153.18
n_lines_expressing: 47
n_dd_up: 0
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 7
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# SH3RF1

*SH3 domain containing ring finger 1* — 4q32.3-q33

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 3.78×; ⚠ cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 2.47×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AsPC-1 2.91×; ⚠ cell-cycle shift, explains ~19% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (HepG2/C3A 2.82×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.323× (z -17.4, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUEDC1]] (+0.61, fdr 1e-05), [[AMIGO2]] (+0.60, fdr 1e-05), [[FHL2]] (+0.60, fdr 7e-06); moves opposite to [[GPR107]] (-0.56, fdr 3e-05), [[AP3S1]] (-0.56, fdr 4e-05), [[SRP54-AS1]] (-0.55, fdr 1e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[KITLG]] → it (grade B ⚠); 7 go from it, the strongest it → [[PTPRK]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7806.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 3.78×; ⚠ cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 2.47×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AsPC-1 2.91×; ⚠ cell-cycle shift, explains ~19% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (HepG2/C3A 2.82×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 1.24× | +3.3 | 0.24 | 21/45 (HepG2/C3A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.24× | +3.3 | 0.24 | 23/45 (AsPC-1, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7806.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.323×** | -17.4 | 0e+00 | 43/45 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.342×** | -16.5 | 0e+00 | 43/45 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.431×** | -13.0 | 4e-36 | 37/46 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.436×** | -12.8 | 3e-35 | 37/45 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.585×** | -11.7 | 2e-29 | 32/46 (C32, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.499×** | -10.3 | 7e-23 | 36/40 (Panc 03.27, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.549×** | -8.5 | 1e-15 | 33/42 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -6.5 | 6e-09 | 32/47 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.691×** | -5.5 | 3e-06 | 29/45 (C32, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.734×** | -4.8 | 1e-04 | 29/45 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.753×** | -4.4 | 7e-04 | 23/45 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.757×** | -4.1 | 0.002 | 24/44 (BT-474, C32, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.833×** | -4.0 | 0.003 | 22/45 (A498, NCI-H1792, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.776×** | -3.9 | 0.004 | 22/45 (A498, SW 900, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.810×** | -3.1 | 0.070 | 22/46 (A498, NCI-H460, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.681×** | -3.1 | 0.070 | 22/44 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.821×** | -3.0 | 0.081 | 20/45 (AN3 CA, RKO, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **0.817×** | -3.0 | 0.092 | 20/45 (SNU-423, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 195 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -19.8) |
| [[KATO III (line)]] | alt | 424 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0710× (z -25.3) |
| [[A-172 (line)]] | wt | 191 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -14.6) |
| [[A498 (line)]] | wt | 185 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -15.4) |
| [[HT-29 (line)]] | alt | 204 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -22.5) |
| [[LOX-IMVI (line)]] | wt | 183 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -21.5) |
| [[J82 (line)]] | alt | 246 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -13.1) |
| [[LoVo (line)]] | wt | 327 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.173× (z -18.9) |
| [[LS 180 (line)]] | wt | 229 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -24.2) |
| [[CFPAC-1 (line)]] | alt | 248 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 204 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -17.5) |
| [[HepG2_C3A (line)]] | wt | 201 | 1 | 5 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.82× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 246 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 246 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 184 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -23.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.175× (z -18.6) |
| [[SW480 (line)]] | alt | 138 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -20.5) |
| [[AsPC-1 (line)]] | alt | 156 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +18.0) ⚠ cell-cycle shift, explains ~34% of this change | [[Panobinostat (drug)]] 5 µM 0.202× (z -15.3) |
| [[A549 (line)]] | wt | 130 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -13.6) |
| [[BT-474 (line)]] | alt | 180 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -14.6) |
| [[PANC-1 (line)]] | alt | 87.4 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.415× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.417× (z -10.2) |
| [[RKO (line)]] | wt | 146 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.342× (z -12.4) |
| [[SW1417 (line)]] | alt | 163 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -16.5) |
| [[COLO 205 (line)]] | alt | 204 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -15.7) |
| [[NCI-H1792 (line)]] | alt | 162 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 152 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -10.2) |
| [[SHP-77 (line)]] | alt | 87.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -11.7) |
| [[SW 900 (line)]] | alt | 140 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.307× (z -11.6) |
| [[C-33 A (line)]] | alt | 75.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.322× (z -9.9) |
| [[CHP-212 (line)]] | wt | 165 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -9.1) |
| [[HOP62 (line)]] | alt | 120 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 52.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.47× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 98.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 46.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -9.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 240 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.291× (z -8.9) |
| [[HS-578T (line)]] | alt | 95.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.0883× (z -18.3) |
| [[SNU-423 (line)]] | alt | 68.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.379× (z -8.8) |
| [[SW 1088 (line)]] | alt | 95.3 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.0709× (z -9.1) |
| [[SW 1271 (line)]] | alt | 96.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0818× (z -9.6) |
| [[SW48 (line)]] | wt | 81.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 81.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.0 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUEDC1]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[AMIGO2]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[FHL2]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[GPR39]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SCHIP1]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[ENC1]] | +0.55 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[FJX1]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[RASAL2]] | +0.54 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[DDAH1]] | +0.54 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[MIR100HG]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PTPRK]] | +0.53 | +0.43 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR107]] | -0.56 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[AP3S1]] | -0.56 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[SRP54-AS1]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[CD109]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[C20orf96]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[PPP1CB]] | -0.53 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[UBAC1]] | -0.52 | -0.47 / -0.44 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[MARCHF6]] | -0.52 | -0.47 / -0.38 | both halves | 6e-05 | same gene group |
| [[HACE1]] | -0.52 | -0.41 / -0.52 | both halves | 4e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[HSPB11]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[HELZ]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[IL17RC]] | -0.50 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KITLG]] | B | KITLG activity raises SH3RF1's level | lines that do not express KITLG (10) vs lines expressing it (40) | 2.24× lower at baseline in the lines without KITLG | 0.017 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[RBPMS]] | B | RBPMS activity raises SH3RF1's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 2.12× lower at baseline in the lines without RBPMS | 0.033 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[DLX1]] | B | DLX1 activity lowers SH3RF1's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 2.15× higher at baseline in the lines without DLX1 | 0.036 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[EVA1A]] | B | EVA1A activity raises SH3RF1's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 1.58× lower at baseline in the lines without EVA1A | 0.041 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[FAM13A]] | B | FAM13A activity raises SH3RF1's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without FAM13A | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[PCED1B]] | B | PCED1B activity raises SH3RF1's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without PCED1B | 0.084 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[ARHGAP42]] | B | ARHGAP42 activity raises SH3RF1's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 1.87× lower at baseline in the lines without ARHGAP42 | 0.089 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[MAMLD1]] | B | MAMLD1 activity weakens SH3RF1's drug response | lines that do not express MAMLD1 (9) vs lines expressing it (38) | the lines without MAMLD1 respond 1.48× as strongly (z diff -2.64); strongest at Dinaciclib 0.5 µM: 0.33x vs 0.50x (z diff -3.3) | 0.098 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1; target measured in part of the lines; artifact flags |
| [[PTPRK]] | C | PTPRK activity raises SH3RF1's level | lines that do not express PTPRK (6) vs lines expressing it (44) | 2.71× lower at baseline in the lines without PTPRK | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000246225, EPS8, ASPH; co-absent with the target |
| [[FHL2]] | C | FHL2 activity raises SH3RF1's level | lines that do not express FHL2 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without FHL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EPS8, MYO1E, RUNX1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRK]] | C | SH3RF1 activity raises PTPRK's level | lines that do not express SH3RF1 (3) vs lines expressing it (47) | 6.63× lower at baseline in the lines without SH3RF1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; co-absent with the target; its own permutation p |
| [[ARHGAP42]] | C | SH3RF1 activity raises ARHGAP42's level | lines that do not express SH3RF1 (3) vs lines expressing it (47) | 5.62× lower at baseline in the lines without SH3RF1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; its own permutation p |
| [[KITLG]] | C | SH3RF1 activity raises KITLG's level | lines that do not express SH3RF1 (3) vs lines expressing it (47) | 5.31× lower at baseline in the lines without SH3RF1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; its own permutation p |
| [[SRP54-AS1]] | C | SH3RF1 activity lowers SRP54-AS1's level | lines that do not express SH3RF1 (3) vs lines expressing it (47) | 2.56× higher at baseline in the lines without SH3RF1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; its own permutation p |
| [[FRMD5]] | C | SH3RF1 activity raises FRMD5's level | lines that do not express SH3RF1 (3) vs lines expressing it (47) | 3.88× lower at baseline in the lines without SH3RF1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; its own permutation p |
| [[PCED1B]] | C | SH3RF1 activity raises PCED1B's level | lines that do not express SH3RF1 (3) vs lines expressing it (47) | 3.86× lower at baseline in the lines without SH3RF1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; its own permutation p |
| [[DLX1]] | C | SH3RF1 activity lowers DLX1's level | lines that do not express SH3RF1 (3) vs lines expressing it (47) | 3.28× higher at baseline in the lines without SH3RF1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; its own permutation p |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.4, 14.0); signed map (15.6, 41.9). **Vector** length 112, 35.2% of its response variance represented; |z| ≥ 3 in 1,325 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +6.4 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.0 | +0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +1.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.6 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +1.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.0 | +0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.9 | +2.1 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -4.0 | -4.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.1 | -2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.8 | -0.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain containing ring finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.3-q33 — chr4:169,094,259-169,270,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | POSH, RNF142, KIAA1494; previously SH3MD2 |
| Gene groups (HGNC) | Ring finger proteins; SH3 domain containing; SH3 domain containing ring finger family |
| Reactome | 7 pathways, smallest: RHOV GTPase cycle; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6J0](https://www.uniprot.org/uniprotkb/Q7Z6J0) (E3 ubiquitin-protein ligase SH3RF1):

> Has E3 ubiquitin-protein ligase activity. In the absence of an external substrate, it can catalyze self-ubiquitination. Stimulates ubiquitination of potassium channel KCNJ1, enhancing its dynamin-dependent and clathrin-independent endocytosis. Acts as a scaffold protein that coordinates with MAPK8IP1/JIP1 in organizing different components of the JNK pathway, including RAC1 or RAC2, MAP3K11/MLK3 or MAP3K7/TAK1, MAP2K7/MKK7, MAPK8/JNK1 and/or MAPK9/JNK2 into a functional multiprotein complex to …

**Summary**, from NCBI Gene [57630](https://www.ncbi.nlm.nih.gov/gene/57630):

> This gene encodes a protein containing an N-terminus RING-finger, four SH3 domains, and a region implicated in binding of the Rho GTPase Rac. Via the RING-finger, the encoded protein has been shown to function as an ubiquitin-protein ligase involved in protein sorting at the trans-Golgi network. The encoded protein may also act as a scaffold for the c-Jun N-terminal kinase signaling pathway, facilitating the formation of a functional signaling module. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17650](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17650) · Entrez [57630](https://www.ncbi.nlm.nih.gov/gene/57630) · UniProt [Q7Z6J0](https://www.uniprot.org/uniprotkb/Q7Z6J0) · Ensembl [ENSG00000154447](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154447)

## Data

Gene col 7806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7806); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7806]; `tensor/DDL_lfc|DDL_z.npy` [7806]; `embed/gene_vectors.npy` [7806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7806 or target_col == 7806). Every well: [[SH3RF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3RF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
