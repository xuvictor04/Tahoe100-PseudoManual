---
symbol: "WDR11"
type: "gene"
col: 4149
ensembl_id: "ENSG00000120008"
name: "WD repeat domain 11"
location: "10q26.12"
module: 17
arm: "+"
pooled_cpm: 87.38
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# WDR11

*WD repeat domain 11* — 10q26.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.28× (z +7.9, q 2e-12, up in 29 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (SNU-1 2.10×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HS-578T 2.74×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (KATO III 1.52×; ⚠ cell-cycle shift, explains ~35% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.414× (z -28.6, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BBS5]] (+0.69, fdr 7e-06), [[DYNC2LI1]] (+0.66, fdr 1e-05), [[MRPS31P4]] (+0.65, fdr 1e-05); moves opposite to [[SAXO1]] (-0.55, fdr 4e-05), [[PKNOX1]] (-0.53, fdr 9e-05), [[SATB2]] (-0.52, fdr 7e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4149.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (SNU-1 2.10×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HS-578T 2.74×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (KATO III 1.52×; ⚠ cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.28×** | +7.9 | 2e-12 | 29/47 (KATO III, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.27×** | +5.4 | 2e-05 | 31/47 (KATO III, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.6 | 7e-04 | 18/47 (J82, A-427, …) | rises with dose | composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.9 | 0.012 | 17/44 (SW 900, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.062 | 19/47 (HS-578T, A498, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.089 | 11/47 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.10× | +3.0 | 0.21 | 2/47 (AN3 CA, SNU-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4149.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.414×** | -28.6 | 0e+00 | 45/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.697×** | -8.3 | 4e-14 | 38/47 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.704×** | -7.7 | 2e-12 | 36/47 (NCI-H460, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -6.8 | 1e-09 | 32/49 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.744×** | -6.8 | 1e-09 | 25/48 (RKO, SNU-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.767×** | -5.6 | 2e-06 | 27/44 (LS 180, SNU-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.788×** | -5.3 | 1e-05 | 24/43 (SHP-77, NCI-H1792, …) | all doses, flat | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.867× | -4.6 | 2e-04 | 12/47 (Hs 766T, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.869× | -4.6 | 3e-04 | 17/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **0.827×** | -4.4 | 7e-04 | 23/47 (SW 1271, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.824×** | -4.3 | 1e-03 | 23/46 (SHP-77, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.842× | -3.9 | 0.004 | 19/47 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | 0.845× | -3.9 | 0.005 | 19/47 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.891× | -3.8 | 0.007 | 16/47 (J82, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.869× | -3.2 | 0.049 | 17/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.908× | -3.1 | 0.059 | 5/47 (SW 900, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 112 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -37.4) |
| [[KATO III (line)]] | alt | 149 | 1 (1 ⚠) | 3 | [[Selinexor (drug)]] 5 µM 1.52× (z +8.6) ⚠ cell-cycle shift, explains ~35% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -32.8) |
| [[A549 (line)]] | wt | 102 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -22.8) |
| [[AsPC-1 (line)]] | alt | 70.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -14.7) |
| [[SHP-77 (line)]] | alt | 79.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -24.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -12.1) |
| [[SNU-1 (line)]] | wt | 129 | 1 | 2 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.10× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.0) |
| [[SW480 (line)]] | alt | 112 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -21.3) |
| [[AN3 CA (line)]] | alt | 170 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -15.2) |
| [[HCT15 (line)]] | alt | 98.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 94.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -14.5) |
| [[HS-578T (line)]] | alt | 61.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -8.8) |
| [[LS 180 (line)]] | wt | 106 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 52.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.400× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -17.6) |
| [[NCI-H23 (line)]] | alt | 66.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -19.6) |
| [[NCI-H596 (line)]] | alt | 92.0 | 0 | 2 (1 ⚠) | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.216× (z -9.2) |
| [[PANC-1 (line)]] | alt | 134 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -17.5) |
| [[RKO (line)]] | wt | 102 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0922× (z -24.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -17.1) |
| [[SK-MEL-2 (line)]] | alt | 109 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -13.6) |
| [[SNU-423 (line)]] | alt | 130 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.379× (z -13.0) |
| [[A-427 (line)]] | wt | 73.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.449× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 32.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -11.8) |
| [[C-33 A (line)]] | alt | 67.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -9.3) |
| [[C32 (line)]] | wt | 69.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -12.8) |
| [[CFPAC-1 (line)]] | alt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -18.8) |
| [[COLO 205 (line)]] | alt | 75.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -13.9) |
| [[H4 (line)]] | wt | 81.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 93.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -10.6) |
| [[HOP62 (line)]] | alt | 46.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -9.9) |
| [[Hs 766T (line)]] | wt | 109 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -22.0) |
| [[HT-29 (line)]] | alt | 63.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -21.0) |
| [[hTERT-HPNE (line)]] | wt | 80.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -10.6) |
| [[J82 (line)]] | alt | 55.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -12.9) |
| [[LoVo (line)]] | wt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -21.9) |
| [[LOX-IMVI (line)]] | wt | 79.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 100 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 56.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 82.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -19.6) |
| [[RPMI-7951 (line)]] | alt | 89.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -15.7) |
| [[SW 1271 (line)]] | alt | 86.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.147× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SW 900 (line)]] | alt | 98.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -13.1) |
| [[SW1417 (line)]] | alt | 85.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -14.5) |
| [[A-172 (line)]] | wt | 16.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 92.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBS5]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[DYNC2LI1]] | +0.66 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[MRPS31P4]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CDC16]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ACTR10]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[UBXN2B]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TRAPPC11]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 | STRING 684 |
| [[ADH5]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[CRBN]] | +0.63 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[MRS2]] | +0.62 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[NDUFA12]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[APOOL]] | +0.61 | +0.50 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAXO1]] | -0.55 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[PKNOX1]] | -0.53 | -0.36 / -0.57 | both halves | 9e-05 |  |
| [[SATB2]] | -0.52 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[CFL1]] | -0.52 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[LINC02798]] | -0.52 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[PELO-AS1]] | -0.50 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[EOLA2-DT]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises WDR11's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.9, -2.9); signed map (-23.0, -15.0). **Vector** length 104, 25.8% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +9.1 | +7.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.9 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +5.0 | -6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +4.9 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +2.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -28.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -8.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -4.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.12 — chr10:120,851,305-120,909,524 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1351, FLJ10506, WDR15, HH14, DR11, SRI1; previously BRWD2 |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 4 pathways, smallest: RHOH GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZH6](https://www.uniprot.org/uniprotkb/Q9BZH6) (WD repeat-containing protein 11):

> Involved in the Hedgehog (Hh) signaling pathway, is essential for normal ciliogenesis. Regulates the proteolytic processing of GLI3 and cooperates with the transcription factor EMX1 in the induction of downstream Hh pathway gene expression and gonadotropin-releasing hormone production. WDR11 complex facilitates the tethering of Adaptor protein-1 complex (AP-1)-derived vesicles. WDR11 complex acts together with TBC1D23 to facilitate the golgin-mediated capture of vesicles generated using AP-1.

**Summary**, from NCBI Gene [55717](https://www.ncbi.nlm.nih.gov/gene/55717):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. This gene is located in the chromosome 10q25-26 region, which is frequently …

**Accessions** — [HGNC:13831](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13831) · Entrez [55717](https://www.ncbi.nlm.nih.gov/gene/55717) · UniProt [Q9BZH6](https://www.uniprot.org/uniprotkb/Q9BZH6) · Ensembl [ENSG00000120008](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120008)

## Data

Gene col 4149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4149); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4149]; `tensor/DDL_lfc|DDL_z.npy` [4149]; `embed/gene_vectors.npy` [4149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4149 or target_col == 4149). Every well: [[WDR11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
