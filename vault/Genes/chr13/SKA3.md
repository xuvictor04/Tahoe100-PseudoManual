---
symbol: "SKA3"
type: "gene"
col: 9127
ensembl_id: "ENSG00000165480"
name: "spindle and kinetochore associated complex subunit 3"
location: "13q12.11"
module: 22
arm: "+"
pooled_cpm: 16.39
n_lines_expressing: 47
n_dd_up: 24
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 16
direction_downstream: 66
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SKA3

*spindle and kinetochore associated complex subunit 3* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (23 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.88× (z +13.4, q 3e-38, up in 20 of 24 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.33× (z +3.7, q 0.005, up in 8 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 3.50×, KATO III 4.96×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 2.68×, Panc 03.27 4.21×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 2.92×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.528× (z -8.4, q 2e-14, down in 28 of 44 measured lines) ⚠ cell-cycle shift, explains ~76% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.654× (z -5.6, q 2e-06, down in 20 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPH]] (+0.91, fdr 7e-06), [[PLK4]] (+0.90, fdr 7e-06), [[KIF15]] (+0.89, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); 66 go from it, the strongest it → [[DIAPH3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 24 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9127.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 3.50×, KATO III 4.96×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 2.68×, Panc 03.27 4.21×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 2.92×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.88×** | +13.4 | 3e-38 | 20/24 (Panc 03.27, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **2.49×** | +12.0 | 8e-31 | 28/36 (SW480, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **1.74×** | +6.7 | 3e-09 | 15/29 (HT-29, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.44×** | +6.7 | 3e-09 | 28/45 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.65×** | +6.3 | 3e-08 | 26/44 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.61×** | +6.3 | 3e-08 | 27/43 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +6.1 | 1e-07 | 25/41 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.52×** | +5.5 | 3e-06 | 19/44 (LoVo, hTERT-HPNE, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.51×** | +5.5 | 3e-06 | 21/45 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~90% of this change | **1.51×** | +5.4 | 4e-06 | 21/39 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.47×** | +5.1 | 2e-05 | 19/44 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.45×** | +4.9 | 4e-05 | 19/44 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.44×** | +4.8 | 7e-05 | 20/45 (LoVo, LS 180, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~95% of this change | **1.46×** | +4.8 | 8e-05 | 15/40 (SNU-1, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +4.5 | 3e-04 | 16/45 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.005 | 8/45 (A498, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9127.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.528×** | -8.4 | 2e-14 | 28/44 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.711×** | -6.4 | 5e-08 | 26/45 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.516×** | -6.2 | 8e-08 | 26/45 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.620×** | -5.7 | 2e-06 | 23/43 (PANC-1, LS 180, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.654×** | -5.6 | 2e-06 | 20/44 (C-33 A, NCI-H2030, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -4.8 | 2e-04 | 22/43 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.707×** | -4.6 | 4e-04 | 21/45 (Hs 766T, RKO, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.821×** | -3.7 | 0.015 | 12/45 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | position effect removed |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.694×** | -3.4 | 0.034 | 11/45 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | 0.833× | -3.4 | 0.034 | 11/45 (HCT15, COLO 205, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.613×** | -3.4 | 0.034 | 11/42 (SW480, H4, …) | two highest doses | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.776×** | -3.4 | 0.034 | 10/44 (SNU-423, HOP62, …) | inconsistent across doses | position effect removed |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.776×** | -3.4 | 0.034 | 8/44 (NCI-H23, SNU-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.759×** | -3.3 | 0.043 | 9/44 (LS 180, A-427, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.788×** | -3.2 | 0.059 | 12/42 (Hs 766T, RPMI-7951, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.778×** | -3.0 | 0.090 | 6/45 (Hs 766T, COLO 205, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.650×** | -3.0 | 0.090 | 13/41 (LoVo, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.779×** | -3.0 | 0.090 | 9/44 (SW 1271, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9127. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 20.5 | 0 | 6 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0864× (z -24.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -13.5) |
| [[LS 180 (line)]] | wt | 17.1 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.128× (z -14.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.252× (z -9.4) |
| [[A-172 (line)]] | wt | 16.5 | 0 | 3 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.164× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 25.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.388× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 13.7 | 0 | 3 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.127× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 27.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 20.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[RKO (line)]] | wt | 25.7 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.318× (z -9.7) |
| [[SNU-1 (line)]] | wt | 14.8 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.109× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 45.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -12.2) |
| [[HOP62 (line)]] | alt | 20.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -11.4) |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.112× (z -10.9) ⚠ cell-cycle shift, explains ~99% of this change |
| [[KATO III (line)]] | alt | 19.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.96× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.50× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -8.6) |
| [[A549 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9127), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPH]] | +0.91 | +0.88 / +0.90 | both halves | 7e-06 | STRING 814 |
| [[PLK4]] | +0.90 | +0.90 / +0.90 | both halves | 7e-06 | STRING 525 |
| [[KIF15]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 | STRING 636 |
| [[SKA1]] | +0.89 | +0.87 / +0.87 | both halves | 7e-06 | STRING 999 |
| [[NCAPG]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | STRING 779 |
| [[AURKB]] | +0.87 | +0.88 / +0.84 | both halves | 7e-06 | STRING 785 |
| [[MELK]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | STRING 718 |
| [[PBK]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | STRING 675 |
| [[POLQ]] | +0.86 | +0.86 / +0.84 | both halves | 7e-06 | STRING 422 |
| [[GINS1]] | +0.86 | +0.88 / +0.85 | both halves | 7e-06 | STRING 445 |
| [[MAD2L1]] | +0.85 | +0.84 / +0.82 | both halves | 7e-06 | STRING 555 |
| [[CENPU]] | +0.85 | +0.82 / +0.85 | both halves | 7e-06 | STRING 617 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 4, C 12. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises SKA3's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.74× lower at baseline in the lines without CDC25A | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises SKA3's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.79× lower at baseline in the lines without FAM111B | 0.013 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises SKA3's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.40× lower at baseline in the lines without E2F8 | 0.029 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises SKA3's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.37× lower at baseline in the lines without CDCA7 | 0.058 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[TCF19]] | C | TCF19 activity raises SKA3's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 3.04× lower at baseline in the lines without TCF19 | 0.004 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent; co-absent with the target |
| [[AURKB]] | C | AURKB activity raises SKA3's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.57× lower at baseline in the lines without AURKB | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[MCM10]] | C | MCM10 activity raises SKA3's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.92× lower at baseline in the lines without MCM10 | 0.014 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises SKA3's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.65× lower at baseline in the lines without DSCC1 | 0.020 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises SKA3's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.87× lower at baseline in the lines without NDC80 | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[PKMYT1]] | C | PKMYT1 activity raises SKA3's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 3.54× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises SKA3's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 3.31× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CLSPN]] | C | CLSPN activity raises SKA3's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 3.01× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*66 arrows, 66 of them with an alert ⚠; grade A 0, B 0, C 66. Shown: the 12 strongest; 54 more arrows (54 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIAPH3]] | C | [[C21orf58]], SKA3 activity raises DIAPH3's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 3.95× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[AURKB]] | C | [[C21orf58]], SKA3 activity raises AURKB's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 3.92× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[TOP2A]] | C | SKA3 activity raises TOP2A's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 3.92× lower at baseline in the lines without SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p |
| [[CLSPN]] | C | [[CDC45]], [[CENPM]], SKA3 activity raises CLSPN's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.82× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CENPF]] | C | SKA3 activity raises CENPF's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 3.78× lower at baseline in the lines without SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p |
| [[FOXM1]] | C | [[C21orf58]], SKA3 activity raises FOXM1's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 3.66× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[KIF18B]] | C | [[C21orf58]], SKA3 activity raises KIF18B's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 3.64× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CKAP2]] | C | SKA3 activity raises CKAP2's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 3.42× lower at baseline in the lines without SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[MKI67]] | C | SKA3 activity raises MKI67's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 3.41× lower at baseline in the lines without SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[GINS1]] | C | [[C21orf58]], [[CDC45]], [[CENPM]], SKA3 activity raises GINS1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.31× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[SPC25]] | C | [[C21orf58]], [[CDC45]], [[CENPM]], SKA3 activity raises SPC25's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.15× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[TK1]] | C | [[C21orf58]], [[CDC45]], [[CENPM]], SKA3 activity raises TK1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.92× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.2, -51.7); signed map (-45.2, -44.2). **Vector** length 123, 34.8% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.64 to 60); *DREAM G2/M down* (control, mean cos +0.66 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.63 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +3.8 | +13.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.7 | +4.3 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +3.6 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +3.5 | +12.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +3.4 | +3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.5 | +3.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.9 | +1.9 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +1.8 | +1.5 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.8 | +1.3 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -6.4 | -8.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.3 | -6.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | -5.5 | -5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -5.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | spindle and kinetochore associated complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:21,153,595-21,176,552 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4832, RAMA1; previously C13orf3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IX90](https://www.uniprot.org/uniprotkb/Q8IX90) (Spindle and kinetochore-associated protein 3):

> Component of the SKA1 complex, a microtubule-binding subcomplex of the outer kinetochore that is essential for proper chromosome segregation. The SKA1 complex is a direct component of the kinetochore-microtubule interface and directly associates with microtubules as oligomeric assemblies. The complex facilitates the processive movement of microspheres along a microtubule in a depolymerization-coupled manner. In the complex, it mediates the microtubule-stimulated oligomerization. Affinity for …

**Summary**, from NCBI Gene [221150](https://www.ncbi.nlm.nih.gov/gene/221150):

> This gene encodes a component of the spindle and kinetochore-associated protein complex that regulates microtubule attachment to the kinetochores during mitosis. The encoded protein localizes to the outer kinetechore and may be required for normal chromosome segregation and cell division. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:20262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20262) · Entrez [221150](https://www.ncbi.nlm.nih.gov/gene/221150) · UniProt [Q8IX90](https://www.uniprot.org/uniprotkb/Q8IX90) · Ensembl [ENSG00000165480](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165480)

## Data

Gene col 9127: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9127); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9127, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9127]; `tensor/DDL_lfc|DDL_z.npy` [9127]; `embed/gene_vectors.npy` [9127]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9127 or target_col == 9127). Every well: [[SKA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SKA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
