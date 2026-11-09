---
symbol: "PIF1"
type: "gene"
col: 6410
ensembl_id: "ENSG00000140451"
name: "PIF1 5'-to-3' DNA helicase"
location: "15q22.31"
module: 22
arm: "+"
pooled_cpm: 11.47
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 55
n_dd_up_clean: 2
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PIF1

*PIF1 5'-to-3' DNA helicase* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 2.85× (z +6.9, q 3e-09, up in 26 of 42 measured lines) ⚠ cell-cycle shift, explains ~76% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +5.9, q 1e-06, up in 24 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2030 5.23×, NCI-H2347 4.01×, Panc 03.27 5.78×, PANC-1 2.75×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 55 drug-doses (22 with an alert ⚠); the strongest is [[Cytarabine (hydrochloride) (drug)]] 0.5 µM: 0.340× (z -13.5, q 6e-39, down in 40 of 46 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Amsacrine (drug)]] 5 µM: 0.545× (z -10.7, q 6e-25, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TROAP]] (+0.90, fdr 7e-06), [[KIF20A]] (+0.88, fdr 7e-06), [[DLGAP5]] (+0.87, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[NEURL1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6410.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2030 5.23×, NCI-H2347 4.01×, Panc 03.27 5.78×, PANC-1 2.75×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **2.85×** | +6.9 | 3e-09 | 26/42 (NCI-H1573, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.9 | 1e-06 | 24/45 (LoVo, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +5.6 | 4e-06 | 22/46 (NCI-H2030, NCI-H2347, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.39×** | +4.1 | 0.004 | 18/43 (NCI-H23, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.38×** | +4.1 | 0.004 | 9/45 (KATO III, NCI-H23, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.37×** | +4.0 | 0.005 | 13/45 (H4, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +4.0 | 0.005 | 11/46 (KATO III, NCI-H2347, …) | all doses, flat | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.25×** | +4.0 | 0.005 | 7/47 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.33×** | +3.6 | 0.021 | 10/47 (NCI-H23, H4, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.31×** | +3.4 | 0.033 | 6/46 (HT-29, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.30×** | +3.3 | 0.045 | 11/41 (HT-29, HOP62, …) | all doses, flat | low cells (technical?); position effect removed |
| [[AZD1390 (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.045 | 14/47 (Panc 03.27, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 22 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 55 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6410.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.340×** | -13.5 | 6e-39 | 40/46 (A549, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.344×** | -12.9 | 2e-35 | 36/45 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.349×** | -12.7 | 1e-34 | 34/45 (SHP-77, HT-29, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.386×** | -11.3 | 2e-27 | 34/46 (HEC-1-A, A-427, …) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.544×** | -10.8 | 5e-25 | 32/47 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **0.545×** | -10.7 | 6e-25 | 33/47 (PANC-1, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.452×** | -9.9 | 2e-21 | 34/47 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.469×** | -8.8 | 1e-16 | 31/46 (A-427, HCT15, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.509×** | -8.5 | 2e-15 | 29/46 (HCT15, NCI-H2030, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.519×** | -8.2 | 1e-14 | 25/45 (A-172, A549, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.324×** | -7.4 | 7e-12 | 26/35 (A549, HOP62, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.544×** | -7.0 | 9e-11 | 28/46 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.573×** | -7.0 | 1e-10 | 27/46 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.578×** | -6.9 | 3e-10 | 27/46 (LS 180, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.586×** | -6.7 | 8e-10 | 24/46 (LS 180, SNU-1, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.671×** | -6.7 | 9e-10 | 26/47 (SK-MEL-2, LOX-IMVI, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.374×** | -6.5 | 4e-09 | 24/45 (HEC-1-A, A549, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.665×** | -5.1 | 1e-05 | 20/43 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.679×** | -4.8 | 4e-05 | 19/46 (NCI-H1573, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.690×** | -4.6 | 9e-05 | 17/46 (C32, A-427, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.696×** | -4.5 | 1e-04 | 20/46 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.511×** | -4.4 | 3e-04 | 14/47 (HOP62, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | **0.724×** | -4.1 | 0.001 | 16/47 (NCI-H1573, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -4.0 | 0.001 | 13/47 (A-427, LoVo, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.718×** | -4.0 | 0.002 | 11/46 (HEC-1-A, A549, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.643×** | -3.9 | 0.002 | 7/47 (SW480, NCI-H1573, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.69 per unit of S-phase module lfc, +1.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 14.2 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.132× (z -14.2) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.230× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 14.4 | 0 | 5 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.140× (z -10.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[PF-06260933 (drug)]] 5 µM 0.0293× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0922× (z -15.1) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.173× (z -11.1) |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0740× (z -15.1) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.194× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 14.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -9.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 11.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Amsacrine (drug)]] 5 µM 0.253× (z -12.2) |
| [[A-427 (line)]] | wt | 14.2 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.134× (z -9.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 6.90 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.110× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 10.3 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | [[Amsacrine (drug)]] 5 µM 0.213× (z -10.5) |
| [[RKO (line)]] | wt | 7.76 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0452× (z -10.4) |
| [[A-172 (line)]] | wt | 7.07 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0198× (z -14.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[C32 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0537× (z -12.5) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0562× (z -9.3) ⚠ cell-cycle shift, explains ~83% of this change |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0357× (z -10.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.290× (z -8.9) ⚠ cell-cycle shift, explains ~71% of this change |
| [[NCI-H1792 (line)]] | alt | 9.87 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.101× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 7.45 | 0 | 1 (1 ⚠) | — | [[Cytarabine (hydrochloride) (drug)]] 5 µM 0.111× (z -9.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 9.24 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -9.3) |
| [[SHP-77 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.156× (z -8.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 9.78 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.211× (z -8.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[AN3 CA (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TROAP]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | STRING 711 |
| [[KIF20A]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[DLGAP5]] | +0.87 | +0.88 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[CDCA8]] | +0.87 | +0.86 / +0.86 | both halves | 7e-06 | STRING 409 |
| [[FAM72D]] | +0.87 | +0.80 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[PTTG1]] | +0.86 | +0.89 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[FAM83D]] | +0.86 | +0.84 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CCNB1]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 | STRING 415 |
| [[PRR11]] | +0.86 | +0.86 / +0.86 | both halves | 7e-06 |  |
| [[NEK2]] | +0.86 | +0.88 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[CCNB2]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 403 |
| [[CDCA3]] | +0.86 | +0.81 / +0.85 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL1B]] | B | NEURL1B activity raises PIF1's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without NEURL1B | 0.012 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[TOP2A]] | B | TOP2A activity raises PIF1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 9.8% of all compounds | 0.020 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PIMREG]] | B | PIMREG activity raises PIF1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without PIMREG | 0.021 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises PIF1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without NDC80 | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PBK]] | C | PBK activity raises PIF1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.38× lower at baseline in the lines without PBK | 0.043 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises PIF1's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]] | C | CDCA3 activity raises PIF1's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.96× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |
| [[ACBD7]] | C | ACBD7 activity raises PIF1's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without ACBD7 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.840). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.6, -57.7); signed map (-51.5, -42.0). **Vector** length 133, 38.2% of its response variance represented; |z| ≥ 3 in 1,261 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.67 to 60); *DREAM G2/M down* (control, mean cos +0.80 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.62 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +4.7 | +3.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +4.6 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +5.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | +3.6 | +4.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.8 | +2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.3 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.5 |
| fall | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.5 | -12.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -6.5 | -13.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -6.2 | -8.5 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -6.2 | -12.7 |
|  | [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -5.7 | -9.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.1 | -10.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -4.8 | -8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -4.5 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -4.2 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | PIF1 5'-to-3' DNA helicase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:64,815,632-64,825,668 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22692; previously C15orf20 |
| Gene groups (HGNC) | Helicases |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 5 pathways, smallest: Telomere Extension By Telomerase; Extension of Telomeres; Telomere Maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H611](https://www.uniprot.org/uniprotkb/Q9H611) (ATP-dependent DNA helicase PIF1):

> DNA-dependent ATPase and 5'-3' DNA helicase required for the maintenance of both mitochondrial and nuclear genome stability. Efficiently unwinds G-quadruplex (G4) DNA structures and forked RNA-DNA hybrids. Resolves G4 structures, preventing replication pausing and double-strand breaks (DSBs) at G4 motifs. Involved in the maintenance of telomeric DNA. Inhibits telomere elongation, de novo telomere formation and telomere addition to DSBs via catalytic inhibition of telomerase. Reduces the …

**Summary**, from NCBI Gene [80119](https://www.ncbi.nlm.nih.gov/gene/80119):

> This gene encodes a DNA-dependent adenosine triphosphate (ATP)-metabolizing enzyme that functions as a 5' to 3' DNA helicase. The encoded protein can resolve G-quadruplex structures and RNA-DNA hybrids at the ends of chromosomes. It also prevents telomere elongation by inhibiting the actions of telomerase. Alternative splicing and the use of alternative start codons results in multiple isoforms that are differentially localized to either the mitochondria or the nucleus. [provided by RefSeq, Nov …

**Accessions** — [HGNC:26220](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26220) · Entrez [80119](https://www.ncbi.nlm.nih.gov/gene/80119) · UniProt [Q9H611](https://www.uniprot.org/uniprotkb/Q9H611) · Ensembl [ENSG00000140451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140451)

## Data

Gene col 6410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6410); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6410]; `tensor/DDL_lfc|DDL_z.npy` [6410]; `embed/gene_vectors.npy` [6410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6410 or target_col == 6410). Every well: [[PIF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
