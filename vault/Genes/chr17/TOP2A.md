---
symbol: "TOP2A"
type: "gene"
col: 5239
ensembl_id: "ENSG00000131747"
name: "DNA topoisomerase II alpha"
location: "17q21.2"
module: 22
arm: "+"
pooled_cpm: 365.75
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 31
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 10
direction_downstream: 4166
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# TOP2A

*DNA topoisomerase II alpha* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.63× (z +9.7, q 2e-19, up in 42 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.42× (z +3.7, q 0.013, up in 30 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (RKO 6.87×, NCI-H2030 3.90×, Panc 03.27 3.76×, PANC-1 3.09×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A549 4.64×, MIA PaCa-2 5.41×, PANC-1 3.25×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 4.09×, A549 3.93×, MIA PaCa-2 4.80×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RKO 3.79×, HS-578T 3.56×).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (19 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.379× (z -13.7, q 3e-40, down in 46 of 46 measured lines) ⚠ cell-cycle shift, explains ~70% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.528× (z -6.7, q 3e-09, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP5]] (+0.96, fdr 7e-06), [[TPX2]] (+0.95, fdr 7e-06), [[KIF4A]] (+0.95, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); 4,166 go from it, the strongest it → [[G2E3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5239.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (RKO 6.87×, NCI-H2030 3.90×, Panc 03.27 3.76×, PANC-1 3.09×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A549 4.64×, MIA PaCa-2 5.41×, PANC-1 3.25×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 4.09×, A549 3.93×, MIA PaCa-2 4.80×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RKO 3.79×, HS-578T 3.56×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **2.63×** | +9.7 | 2e-19 | 42/47 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **2.27×** | +8.3 | 3e-14 | 37/42 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **3.44×** | +6.8 | 2e-09 | 41/45 (J82, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.51×** | +5.9 | 4e-07 | 28/46 (RKO, NCI-H2030, …) | top dose only | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.47×** | +5.6 | 2e-06 | 43/46 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.56×** | +4.7 | 2e-04 | 34/46 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.59×** | +4.5 | 5e-04 | 28/43 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.47×** | +4.1 | 0.003 | 31/46 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.42×** | +3.7 | 0.013 | 30/46 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.049 | 23/46 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 1.34× | +3.1 | 0.10 | 24/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5239.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.379×** | -13.7 | 3e-40 | 46/46 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.397×** | -9.6 | 2e-19 | 46/46 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.357×** | -9.3 | 2e-18 | 41/46 (KATO III, SW48, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.422×** | -9.0 | 3e-17 | 41/46 (KATO III, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **0.287×** | -6.8 | 1e-09 | 41/43 (SHP-77, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.528×** | -6.7 | 3e-09 | 36/46 (Panc 03.27, COLO 205, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.554×** | -6.2 | 6e-08 | 29/46 (H4, LOX-IMVI, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.569×** | -5.9 | 3e-07 | 43/47 (HT-29, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.562×** | -5.8 | 5e-07 | 44/46 (C32, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **0.600×** | -5.1 | 2e-05 | 31/45 (H4, C32, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.612×** | -5.1 | 2e-05 | 39/46 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.707×** | -5.0 | 3e-05 | 37/46 (HCT15, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.624×** | -4.9 | 4e-05 | 29/46 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.628×** | -4.8 | 5e-05 | 30/47 (H4, LOX-IMVI, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.728×** | -4.6 | 2e-04 | 28/46 (H4, A498, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.512×** | -3.7 | 0.008 | 31/46 (AN3 CA, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.513×** | -3.6 | 0.008 | 27/46 (A498, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.1 | 0.043 | 24/46 (A-427, H4, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.747×** | -3.0 | 0.060 | 25/46 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **0.810×** | -3.0 | 0.064 | 19/46 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | **0.817×** | -2.9 | 0.083 | 22/47 (NCI-H460, CFPAC-1, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.662×** | -2.8 | 0.085 | 22/47 (SNU-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.801×** | -2.8 | 0.091 | 21/46 (NCI-H460, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +1.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 277 | 1 (1 ⚠) | 11 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.167× (z -12.0) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.340× (z -10.1) |
| [[H4 (line)]] | wt | 433 | 0 | 12 (8 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.111× (z -17.4) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.147× (z -15.7) |
| [[A-172 (line)]] | wt | 282 | 2 (2 ⚠) | 7 (6 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.09× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | [[Selinexor (drug)]] 5 µM 0.243× (z -14.8) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.419× (z -9.3) |
| [[A498 (line)]] | wt | 448 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.112× (z -26.1) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.396× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 331 | 0 | 8 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.136× (z -17.3) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.170× (z -11.2) |
| [[A549 (line)]] | wt | 583 | 3 (3 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Selinexor (drug)]] 5 µM 0.314× (z -12.0) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.419× (z -9.4) |
| [[KATO III (line)]] | alt | 407 | 3 (3 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.37× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Ixazomib citrate (drug)]] 5 µM 0.172× (z -13.4) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.293× (z -9.4) |
| [[LS 180 (line)]] | wt | 169 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.188× (z -14.2) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.343× (z -9.2) |
| [[SNU-1 (line)]] | wt | 342 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0755× (z -15.1) |
| [[SW48 (line)]] | wt | 393 | 0 | 6 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.188× (z -11.3) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.328× (z -10.5) |
| [[HT-29 (line)]] | alt | 314 | 2 (2 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Selinexor (drug)]] 5 µM 0.288× (z -11.7) ⚠ cell-cycle shift, explains ~70% of this change |
| [[MIA PaCa-2 (line)]] | alt | 396 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 538 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.154× (z -21.5) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.380× (z -11.6) |
| [[HCT15 (line)]] | alt | 570 | 0 | 4 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.150× (z -10.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HEC-1-A (line)]] | alt | 557 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.292× (z -11.3) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.385× (z -8.8) |
| [[HOP62 (line)]] | alt | 564 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.299× (z -12.7) ⚠ cell-cycle shift, explains ~70% of this change |
| [[HS-578T (line)]] | alt | 263 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +8.8) | [[Selinexor (drug)]] 5 µM 0.369× (z -9.4) ⚠ cell-cycle shift, explains ~70% of this change |
| [[PANC-1 (line)]] | alt | 348 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | [[Bortezomib (drug)]] 0.05 µM 0.271× (z -9.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[RKO (line)]] | wt | 197 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +20.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 524 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0709× (z -12.4) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.278× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 200 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.250× (z -11.5) ⚠ cell-cycle shift, explains ~70% of this change |
| [[NCI-H460 (line)]] | wt | 293 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.230× (z -14.3) ⚠ cell-cycle shift, explains ~70% of this change |
| [[Panc 03.27 (line)]] | alt | 365 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +13.6) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.316× (z -11.8) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.301× (z -9.0) |
| [[SW1417 (line)]] | alt | 309 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.376× (z -11.6) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SW480 (line)]] | alt | 532 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Bortezomib (drug)]] 0.05 µM 0.261× (z -9.6) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -8.5) |
| [[LoVo (line)]] | wt | 200 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.262× (z -12.8) ⚠ cell-cycle shift, explains ~70% of this change |
| [[NCI-H2030 (line)]] | alt | 630 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +16.2) ⚠ cell-cycle shift, would explain all of this change | [[Bortezomib (drug)]] 5 µM 0.145× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~52% of this change |
| [[NCI-H2347 (line)]] | alt | 531 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.436× (z -9.8) ⚠ cell-cycle shift, explains ~70% of this change |
| [[AN3 CA (line)]] | alt | 408 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 379 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[CFPAC-1 (line)]] | alt | 369 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.344× (z -9.8) ⚠ cell-cycle shift, explains ~70% of this change |
| [[COLO 205 (line)]] | alt | 178 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.167× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -9.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H1792 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H23 (line)]] | alt | 463 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.351× (z -11.8) ⚠ cell-cycle shift, explains ~70% of this change |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.0719× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 287 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.383× (z -8.6) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SHP-77 (line)]] | alt | 684 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.101× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~52% of this change |
| [[SK-MEL-2 (line)]] | alt | 286 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.305× (z -12.3) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SNU-423 (line)]] | alt | 303 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.261× (z -8.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[AsPC-1 (line)]] | alt | 72.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 268 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 425 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 683 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 468 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 246 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP5]] | +0.96 | +0.96 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 978 |
| [[TPX2]] | +0.95 | +0.96 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 942 |
| [[KIF4A]] | +0.95 | +0.96 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 915 |
| [[KIF18A]] | +0.93 | +0.93 / +0.93 | both halves | 7e-06 | STRING 643 |
| [[BUB1]] | +0.93 | +0.93 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 982 |
| [[BIRC5]] | +0.92 | +0.94 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 976 |
| [[CENPF]] | +0.92 | +0.93 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 974 |
| [[KIF23]] | +0.92 | +0.92 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 927 |
| [[NDC80]] | +0.92 | +0.92 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 876 |
| [[MKI67]] | +0.91 | +0.92 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 993 |
| [[CCNA2]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 982 |
| [[NCAPD2]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 686 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises TOP2A's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.79× lower at baseline in the lines without PIMREG | 0.007 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises TOP2A's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without NEURL1B | 0.099 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[AURKB]] | C | AURKB activity raises TOP2A's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.82× lower at baseline in the lines without AURKB | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises TOP2A's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.36× lower at baseline in the lines without PBK | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[NDC80]] | C | NDC80 activity raises TOP2A's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without NDC80 | 0.043 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[DIAPH3]] | C | DIAPH3 activity raises TOP2A's level | lines that do not express DIAPH3 (3) vs lines expressing it (47) | 3.99× lower at baseline in the lines without DIAPH3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SKA3]] | C | SKA3 activity raises TOP2A's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 3.92× lower at baseline in the lines without SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises TOP2A's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.32× lower at baseline in the lines without CDCA3, SPDL1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises TOP2A's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.86× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[SAPCD2]] | C | SAPCD2 activity raises TOP2A's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.80× lower at baseline in the lines without SAPCD2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4,166 arrows, 4,166 of them with an alert ⚠; grade A 0, B 4,166, C 0. Shown: the 12 strongest; 4,154 more arrows (4,154 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[G2E3]] | B | TOP2A activity raises G2E3's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.5% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[RABL2B]] | B | TOP2A activity lowers RABL2B's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[RASSF8-AS1]] | B | TOP2A activity lowers RASSF8-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ENSG00000285667]] | B | TOP2A activity lowers ENSG00000285667's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[LRRIQ3]] | B | TOP2A activity lowers LRRIQ3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[BAX]] | B | TOP2A activity lowers BAX's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CIBAR1-DT]] | B | TOP2A activity lowers CIBAR1-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ENSG00000287400]] | B | TOP2A activity lowers ENSG00000287400's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MIDEAS]] | B | TOP2A activity raises MIDEAS's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TARID]] | B | TOP2A activity lowers TARID's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ZNF665]] | B | TOP2A activity lowers ZNF665's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[AK1]] | B | TOP2A activity lowers AK1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.960). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.4, -55.8); signed map (-49.6, -43.2). **Vector** length 178, 79.9% of its response variance represented; |z| ≥ 3 in 1,518 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.74 to 48); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.75 to 41); *Mitotic Anaphase* (reactome, mean cos +0.75 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.4 | +5.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +6.9 | +6.8 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | +5.7 | +5.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.7 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +1.5 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.3 | +1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.2 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +0.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -13.1 | -13.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -10.6 | -9.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | -10.6 | -9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -10.2 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -10.0 | -9.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.3 | -4.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | -6.1 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -5.4 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | DNA topoisomerase II alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:40,388,525-40,417,896 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TOP2alpha, TOPIIA; previously TOP2 |
| Gene groups (HGNC) | Topoisomerases |
| Hallmark sets | PEROXISOME, APOPTOSIS, ESTROGEN_RESPONSE_LATE, G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 8 pathways, smallest: Transcription of E2F targets under negative control by DREAM complex; G0 and Early G1; SUMOylation of DNA replication proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P11388](https://www.uniprot.org/uniprotkb/P11388) (DNA topoisomerase 2-alpha):

> Key decatenating enzyme that alters DNA topology by binding to two double-stranded DNA molecules, generating a double-stranded break in one of the strands, passing the intact strand through the broken strand, and religating the broken strand. May play a role in regulating the period length of BMAL1 transcriptional oscillation (By similarity).

**Summary**, from NCBI Gene [7153](https://www.ncbi.nlm.nih.gov/gene/7153):

> This gene encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. This nuclear enzyme is involved in processes such as chromosome condensation, chromatid separation, and the relief of torsional stress that occurs during DNA transcription and replication. It catalyzes the transient breaking and rejoining of two strands of duplex DNA which allows the strands to pass through one another, thus altering the topology of DNA. Two forms of this …

**Accessions** — [HGNC:11989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11989) · Entrez [7153](https://www.ncbi.nlm.nih.gov/gene/7153) · UniProt [P11388](https://www.uniprot.org/uniprotkb/P11388) · Ensembl [ENSG00000131747](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131747)

## Data

Gene col 5239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5239); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5239]; `tensor/DDL_lfc|DDL_z.npy` [5239]; `embed/gene_vectors.npy` [5239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5239 or target_col == 5239). Every well: [[TOP2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOP2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
