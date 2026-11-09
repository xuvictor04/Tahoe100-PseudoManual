---
symbol: "CDK1"
type: "gene"
col: 9933
ensembl_id: "ENSG00000170312"
name: "cyclin dependent kinase 1"
location: "10q21.2"
module: 22
arm: "+"
pooled_cpm: 61.2
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CDK1

*cyclin dependent kinase 1* — 10q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +8.8, q 1e-15, up in 31 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 12 lines (PANC-1 2.95×, Panc 03.27 3.43×, A549 3.58×, AsPC-1 4.46×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 3.91×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 3.81×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.509× (z -9.9, q 2e-20, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~88% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.511× (z -7.0, q 5e-10, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPG]] (+0.94, fdr 7e-06), [[KIF2C]] (+0.92, fdr 7e-06), [[NDC80]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 15 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9933.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 12 lines (PANC-1 2.95×, Panc 03.27 3.43×, A549 3.58×, AsPC-1 4.46×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 3.91×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 3.81×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.81×** | +8.8 | 1e-15 | 31/48 (PANC-1, Panc 03.27, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.82×** | +6.2 | 1e-07 | 38/48 (KATO III, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.76×** | +5.9 | 7e-07 | 36/48 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.65×** | +5.2 | 2e-05 | 39/48 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.61×** | +5.0 | 7e-05 | 26/47 (A549, PANC-1, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~91% of this change | **1.62×** | +4.8 | 1e-04 | 30/47 (J82, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.60×** | +4.7 | 2e-04 | 34/48 (PANC-1, A-427, …) | rises with dose | composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **2.33×** | +4.6 | 3e-04 | 32/47 (PANC-1, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.53×** | +4.4 | 6e-04 | 32/48 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +4.2 | 0.001 | 31/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.48×** | +4.1 | 0.002 | 29/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.45×** | +3.7 | 0.010 | 26/48 (RKO, SW480, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +3.6 | 0.014 | 23/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +3.3 | 0.035 | 23/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +3.1 | 0.067 | 18/47 (H4, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9933.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.509×** | -9.9 | 2e-20 | 41/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.474×** | -7.8 | 2e-12 | 39/48 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.511×** | -7.0 | 5e-10 | 35/48 (AsPC-1, HEC-1-A, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.559×** | -6.0 | 2e-07 | 33/48 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.501×** | -5.9 | 3e-07 | 34/48 (SW48, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **0.422×** | -4.7 | 2e-04 | 32/45 (A-172, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.537×** | -4.6 | 3e-04 | 31/48 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.644×** | -4.6 | 3e-04 | 34/48 (LoVo, COLO 205, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.760×** | -4.0 | 0.003 | 31/48 (Hs 766T, HT-29, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.787×** | -3.5 | 0.023 | 25/48 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **0.804×** | -3.2 | 0.065 | 24/48 (CFPAC-1, NCI-H23, …) | top dose only |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.650×** | -3.2 | 0.065 | 25/48 (SNU-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.691×** | -3.2 | 0.065 | 19/48 (SW480, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +1.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9933. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 68.8 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.184× (z -11.8) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.171× (z -8.7) |
| [[LS 180 (line)]] | wt | 58.6 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.127× (z -15.4) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.243× (z -10.5) |
| [[SW48 (line)]] | wt | 72.0 | 0 | 5 (4 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.139× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.342× (z -9.1) |
| [[A-172 (line)]] | wt | 66.3 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.229× (z -13.9) ⚠ cell-cycle shift, explains ~88% of this change |
| [[A498 (line)]] | wt | 69.4 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.204× (z -17.6) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.420× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 50.9 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.141× (z -16.4) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.210× (z -9.2) |
| [[LoVo (line)]] | wt | 43.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 0.5 µM 0.239× (z -9.6) ⚠ cell-cycle shift, explains ~96% of this change |
| [[NCI-H460 (line)]] | wt | 65.2 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.302× (z -11.4) ⚠ cell-cycle shift, explains ~88% of this change |
| [[SNU-1 (line)]] | wt | 66.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 50.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +12.2) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.200× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 25.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.159× (z -8.6) |
| [[HOP62 (line)]] | alt | 61.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.347× (z -11.5) ⚠ cell-cycle shift, explains ~88% of this change |
| [[HS-578T (line)]] | alt | 33.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 64.1 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 67.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.293× (z -12.3) ⚠ cell-cycle shift, explains ~88% of this change |
| [[A-427 (line)]] | wt | 79.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.138× (z -20.9) ⚠ cell-cycle shift, explains ~88% of this change |
| [[AsPC-1 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 28.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 77.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.278× (z -10.0) ⚠ cell-cycle shift, explains ~88% of this change |
| [[HEC-1-A (line)]] | alt | 79.5 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.358× (z -8.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[J82 (line)]] | alt | 58.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 80.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 65.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 58.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 62.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 92.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 112 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9933), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPG]] | +0.94 | +0.95 / +0.92 | both halves | 7e-06 | pathway: Condensation of Prometaphase Chromosomes; STRING 981 |
| [[KIF2C]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 972 |
| [[NDC80]] | +0.92 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 957 |
| [[TPX2]] | +0.92 | +0.95 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 952 |
| [[KIF11]] | +0.91 | +0.92 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 987 |
| [[DEPDC1B]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | STRING 762 |
| [[TOP2A]] | +0.91 | +0.92 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 997 |
| [[RACGAP1]] | +0.91 | +0.90 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 960 |
| [[MKI67]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 939 |
| [[CDCA8]] | +0.91 | +0.92 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 990 |
| [[KIF15]] | +0.90 | +0.90 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 856 |
| [[NUSAP1]] | +0.90 | +0.91 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 946 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CDK1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.11× lower at baseline in the lines without PIMREG | 0.013 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[PBK]] | C | PBK activity raises CDK1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without PBK | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CDK1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without AURKB | 0.031 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises CDK1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.35× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises CDK1's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 2.38× lower at baseline in the lines without C21orf58, SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises CDK1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.30× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.936). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.4, -55.0); signed map (-48.7, -43.4). **Vector** length 150, 58.1% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.82 to 28); *Mitotic Spindle Checkpoint* (reactome, mean cos +0.72 to 31); *Separation of Sister Chromatids* (reactome, mean cos +0.71 to 34).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.8 | +8.8 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +3.6 | +3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +3.6 | +5.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | +2.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.4 | +2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.7 | -7.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~75% of this change | -9.9 | -5.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | -8.6 | -7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -8.2 | -6.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -7.9 | -9.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.7 | -4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.9 | -2.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.2 — chr10:60,778,331-60,794,852 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDC28A; previously CDC2 |
| Gene groups (HGNC) | Cyclin dependent kinases; Centriolar satellite proteins |
| Hallmark sets | SPERMATOGENESIS, PI3K_AKT_MTOR_SIGNALING, GLYCOLYSIS, G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 73 pathways, smallest: G2/M DNA replication checkpoint; Phosphorylation of Emi1; Activation of NIMA Kinases NEK9, NEK6, NEK7 |
| Matched by | ensembl_id |

**Function**, from UniProt [P06493](https://www.uniprot.org/uniprotkb/P06493) (Cyclin-dependent kinase 1):

> Plays a key role in the control of the eukaryotic cell cycle by modulating the centrosome cycle as well as mitotic onset; promotes G2-M transition via association with multiple interphase cyclins. Phosphorylates PARVA/actopaxin, APC, AMPH, APC, ASB7, BARD1, Bcl-xL/BCL2L1, BRCA2, CALD1, CASP8, CDC7, CDC20, CDC25A, CDC25C, CC2D1A, CENPA, CSNK2 proteins/CKII, FZR1/CDH1, CDK7, CEBPB, CHAMP1, DMD/dystrophin, EEF1 proteins/EF-1, EZH2, KIF11/EG5, EGFR, FANCG, FOS, GFAP, GOLGA2/GM130, GRASP1, …

**Summary**, from NCBI Gene [983](https://www.ncbi.nlm.nih.gov/gene/983):

> The protein encoded by this gene is a member of the Ser/Thr protein kinase family. This protein is a catalytic subunit of the highly conserved protein kinase complex known as M-phase promoting factor (MPF), which is essential for G2/M phase transitions of eukaryotic cell cycle. Mitotic cyclins stably associate with this protein and function as regulatory subunits. The kinase activity of this protein is controlled by cyclin accumulation and destruction through the cell cycle. The phosphorylation …

**Accessions** — [HGNC:1722](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1722) · Entrez [983](https://www.ncbi.nlm.nih.gov/gene/983) · UniProt [P06493](https://www.uniprot.org/uniprotkb/P06493) · Ensembl [ENSG00000170312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170312)

## Data

Gene col 9933: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9933); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9933, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9933]; `tensor/DDL_lfc|DDL_z.npy` [9933]; `embed/gene_vectors.npy` [9933]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9933 or target_col == 9933). Every well: [[CDK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
