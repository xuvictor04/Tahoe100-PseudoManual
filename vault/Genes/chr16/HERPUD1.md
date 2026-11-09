---
symbol: "HERPUD1"
type: "gene"
col: 574
ensembl_id: "ENSG00000051108"
name: "homocysteine inducible ER protein with ubiquitin like domain 1"
location: "16q13"
module: 56
arm: "+"
pooled_cpm: 103.79
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 22
n_dd_up_clean: 8
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# HERPUD1

*homocysteine inducible ER protein with ubiquitin like domain 1* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.24× (z +8.2, q 1e-13, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.403× (z -13.1, q 3e-36, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GFPT1]] (+0.82, fdr 7e-06), [[HSPA5]] (+0.75, fdr 7e-06), [[MKNK2]] (+0.73, fdr 7e-06); moves opposite to [[PRRC2B]] (-0.59, fdr 5e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 574.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.24×** | +8.2 | 1e-13 | 44/48 (A-172, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +7.1 | 5e-10 | 37/48 (SW480, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +5.4 | 2e-05 | 37/48 (SW480, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.52×** | +4.3 | 0.003 | 36/48 (Hs 766T, A-172, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +3.8 | 0.015 | 22/45 (NCI-H2347, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.7 | 0.017 | 25/47 (Panc 03.27, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +3.6 | 0.031 | 27/48 (J82, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.059 | 25/48 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.060 | 24/49 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.086 | 21/48 (HS-578T, RPMI-7951, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +3.1 | 0.086 | 26/48 (SW480, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 574.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.403×** | -13.1 | 3e-36 | 42/49 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.359×** | -10.0 | 4e-21 | 44/48 (hTERT-HPNE, SW 900, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.550×** | -8.6 | 2e-15 | 47/48 (HS-578T, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -7.4 | 2e-11 | 34/41 (HT-29, HCT15, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.601×** | -7.3 | 3e-11 | 38/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.494×** | -7.2 | 8e-11 | 38/49 (SNU-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.471×** | -7.1 | 1e-10 | 33/45 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.525×** | -6.3 | 2e-08 | 39/50 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.538×** | -6.3 | 2e-08 | 38/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.529×** | -6.2 | 3e-08 | 36/48 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.611×** | -5.0 | 3e-05 | 37/48 (CFPAC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.719×** | -4.7 | 1e-04 | 32/48 (J82, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.631×** | -4.5 | 3e-04 | 35/47 (A-172, SW1417, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.565×** | -4.4 | 5e-04 | 35/48 (A-172, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.665×** | -4.1 | 0.001 | 30/48 (KATO III, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.649×** | -4.1 | 0.002 | 30/47 (A549, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.695×** | -3.7 | 0.007 | 34/49 (SNU-1, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.732×** | -3.2 | 0.047 | 25/48 (A-172, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.732×** | -3.2 | 0.047 | 26/47 (C-33 A, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 574. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 123 | 1 | 9 | [[Auranofin (drug)]] 5 µM 4.13× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -18.0) |
| [[HT-29 (line)]] | alt | 212 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -13.4) |
| [[HS-578T (line)]] | alt | 207 | 1 | 7 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.60× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -17.3) |
| [[SW480 (line)]] | alt | 82.1 | 3 | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.76× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -10.3) |
| [[KATO III (line)]] | alt | 251 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0402× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.206× (z -10.7) |
| [[LoVo (line)]] | wt | 154 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.202× (z -12.2) |
| [[H4 (line)]] | wt | 173 | 1 | 4 | [[Panobinostat (drug)]] 0.5 µM 3.62× (z +8.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -12.2) |
| [[Hs 766T (line)]] | wt | 126 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -12.7) |
| [[HOP62 (line)]] | alt | 69.5 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -13.0) |
| [[J82 (line)]] | alt | 109 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -11.1) |
| [[PANC-1 (line)]] | alt | 51.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -14.5) |
| [[A-427 (line)]] | wt | 55.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.8) |
| [[A498 (line)]] | wt | 165 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -14.9) |
| [[A549 (line)]] | wt | 66.4 | 0 | 3 | — | [[Harringtonine (drug)]] 0.05 µM 0.248× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 71.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -23.5) |
| [[HCT15 (line)]] | alt | 234 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0724× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.209× (z -9.3) |
| [[LS 180 (line)]] | wt | 206 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -9.5) |
| [[SNU-1 (line)]] | wt | 91.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.224× (z -10.7) |
| [[SNU-423 (line)]] | alt | 71.0 | 1 | 2 | [[Auranofin (drug)]] 5 µM 4.11× (z +10.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -9.9) |
| [[SW 900 (line)]] | alt | 82.8 | 1 | 2 | [[Auranofin (drug)]] 5 µM 3.91× (z +9.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -13.1) |
| [[CHP-212 (line)]] | wt | 113 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -12.5) |
| [[COLO 205 (line)]] | alt | 130 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.378× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 69.4 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.420× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 104 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -11.3) |
| [[RKO (line)]] | wt | 78.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -12.9) |
| [[SW1417 (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 88.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 29.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.29× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 146 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -11.2) |
| [[NCI-H661 (line)]] | alt | 71.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 48.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.85× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 52.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.3) |
| [[AN3 CA (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 574), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GFPT1]] | +0.82 | +0.82 / +0.76 | both halves | 7e-06 | pathway: Unfolded Protein Response (UPR) |
| [[HSPA5]] | +0.75 | +0.72 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 792 |
| [[MKNK2]] | +0.73 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.72 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.71 | +0.69 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 543 |
| [[SEL1L]] | +0.71 | +0.76 / +0.64 | both halves | 7e-06 | STRING 719 |
| [[CHAC1]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 453 |
| [[COPB1]] | +0.70 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[SSR2]] | +0.70 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[SEC13]] | +0.70 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[PRRC1]] | +0.70 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[MANF]] | +0.69 | +0.69 / +0.64 | both halves | 7e-06 | STRING 632 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC2B]] | -0.59 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises HERPUD1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.9% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.3, -31.4); signed map (-52.8, 9.2). **Vector** length 167, 61.2% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.60 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.59 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.59 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.6 | +8.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +10.7 | +5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +10.6 | +7.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.7 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +4.1 | +4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.4 | +1.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.4 | +2.7 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.6 | -8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -13.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.6 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.3 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.2 | -4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.5 | -4.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.1 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | homocysteine inducible ER protein with ubiquitin like domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,932,142-56,944,864 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0025, Mif1, HERP, SUP; previously HERPUD1-IT1 |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 5 pathways, smallest: ATF4 activates genes in response to endoplasmic reticulum  stress; PERK regulates gene expression; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15011](https://www.uniprot.org/uniprotkb/Q15011) (Homocysteine-responsive endoplasmic reticulum-resident ubiquitin-like domain member 1 protein):

> Component of the endoplasmic reticulum quality control (ERQC) system also called ER-associated degradation (ERAD) involved in ubiquitin-dependent degradation of misfolded endoplasmic reticulum proteins. Could enhance presenilin-mediated amyloid-beta protein 40 generation. Binds to ubiquilins and this interaction is required for efficient degradation of CD3D via the ERAD pathway.

**Summary**, from NCBI Gene [9709](https://www.ncbi.nlm.nih.gov/gene/9709):

> The accumulation of unfolded proteins in the endoplasmic reticulum (ER) triggers the ER stress response. This response includes the inhibition of translation to prevent further accumulation of unfolded proteins, the increased expression of proteins involved in polypeptide folding, known as the unfolded protein response (UPR), and the destruction of misfolded proteins by the ER-associated protein degradation (ERAD) system. This gene may play a role in both UPR and ERAD. Its expression is induced …

**Accessions** — [HGNC:13744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13744) · Entrez [9709](https://www.ncbi.nlm.nih.gov/gene/9709) · UniProt [Q15011](https://www.uniprot.org/uniprotkb/Q15011) · Ensembl [ENSG00000051108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000051108)

## Data

Gene col 574: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 574); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 574, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 574]; `tensor/DDL_lfc|DDL_z.npy` [574]; `embed/gene_vectors.npy` [574]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 574 or target_col == 574). Every well: [[HERPUD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERPUD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
