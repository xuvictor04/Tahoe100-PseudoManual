---
symbol: "NEK2"
type: "gene"
col: 3939
ensembl_id: "ENSG00000117650"
name: "NIMA related kinase 2"
location: "1q32.3"
module: 22
arm: "+"
pooled_cpm: 32.24
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 30
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# NEK2

*NIMA related kinase 2* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.39× (z +14.1, q 3e-42, up in 34 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.13× (z +8.6, q 1e-15, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (16 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.451× (z -8.6, q 5e-15, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.388× (z -5.7, q 1e-06, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CKAP2]] (+0.94, fdr 7e-06), [[CCNB2]] (+0.93, fdr 7e-06), [[DLGAP5]] (+0.93, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3939.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.39×** | +14.1 | 3e-42 | 34/48 (Panc 03.27, HOP62, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.26×** | +9.1 | 2e-17 | 36/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +8.6 | 1e-15 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~84% of this change | **2.00×** | +7.9 | 3e-13 | 37/46 (HT-29, SW 900, …) | all doses, flat | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +7.9 | 4e-13 | 33/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **3.46×** | +7.4 | 1e-11 | 39/46 (PANC-1, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +7.2 | 6e-11 | 30/47 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.71×** | +5.9 | 2e-07 | 30/48 (PANC-1, RKO, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.67×** | +5.6 | 1e-06 | 25/47 (A-172, NCI-H23, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.55×** | +5.0 | 3e-05 | 23/48 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.35×** | +4.9 | 6e-05 | 31/48 (HT-29, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.52×** | +4.8 | 7e-05 | 28/48 (SW 900, HT-29, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.49×** | +4.6 | 2e-04 | 21/48 (PANC-1, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **1.49×** | +4.5 | 2e-04 | 22/44 (A-172, PANC-1, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.46×** | +4.3 | 7e-04 | 21/47 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.002 | 19/48 (HT-29, NCI-H1792, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.025 | 15/48 (H4, KATO III, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.035 | 16/48 (AsPC-1, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 16 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3939.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.451×** | -8.6 | 5e-15 | 36/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.494×** | -8.1 | 2e-13 | 34/47 (SW48, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.521×** | -7.5 | 2e-11 | 35/47 (A498, KATO III, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.562×** | -6.6 | 6e-09 | 35/48 (H4, NCI-H460, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.569×** | -6.2 | 6e-08 | 34/47 (SW48, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.388×** | -5.7 | 1e-06 | 27/47 (SW 900, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.621×** | -5.5 | 4e-06 | 30/47 (SW48, A549, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~67% of this change | **0.427×** | -5.1 | 3e-05 | 26/41 (SHP-77, NCI-H2347, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **0.762×** | -4.4 | 7e-04 | 22/48 (A498, A-172, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.766×** | -4.3 | 9e-04 | 24/48 (A498, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.688×** | -4.3 | 9e-04 | 26/47 (AsPC-1, Panc 03.27, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.691×** | -4.2 | 0.001 | 22/48 (NCI-H460, A549, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.693×** | -4.2 | 0.001 | 22/47 (SW48, A-172, …) | two highest doses |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.694×** | -4.2 | 0.001 | 23/48 (SW48, A549, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.700×** | -3.9 | 0.003 | 22/47 (A549, A498, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -3.8 | 0.005 | 18/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.732×** | -3.6 | 0.010 | 19/47 (SNU-1, A549, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.578×** | -3.3 | 0.029 | 15/46 (RPMI-7951, C32, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.580×** | -3.3 | 0.030 | 14/47 (RPMI-7951, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.736×** | -3.2 | 0.030 | 19/47 (NCI-H1573, A-427, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.756×** | -3.2 | 0.033 | 20/47 (NCI-H1573, HCT15, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.748×** | -3.1 | 0.038 | 11/48 (Panc 03.27, KATO III, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.748×** | -3.1 | 0.045 | 14/47 (NCI-H1573, SW48, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.610×** | -3.0 | 0.063 | 15/46 (C32, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.759×** | -2.9 | 0.069 | 13/47 (NCI-H661, H4, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.837× | -2.9 | 0.072 | 14/48 (LOX-IMVI, SHP-77, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.776×** | -2.8 | 0.094 | 9/47 (A498, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +1.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 43.2 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.210× (z -16.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.378× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 26.8 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0790× (z -13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.183× (z -9.1) |
| [[A-427 (line)]] | wt | 47.8 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.268× (z -13.1) |
| [[C32 (line)]] | wt | 17.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | [[Bortezomib (drug)]] 0.05 µM 0.135× (z -8.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A-172 (line)]] | wt | 25.2 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.167× (z -10.6) ⚠ cell-cycle shift, explains ~97% of this change |
| [[A549 (line)]] | wt | 29.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.222× (z -9.0) ⚠ cell-cycle shift, explains ~97% of this change |
| [[H4 (line)]] | wt | 35.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0411× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 48.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +14.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.105× (z -8.8) ⚠ cell-cycle shift, explains ~97% of this change |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.113× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 45.6 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.107× (z -10.1) ⚠ cell-cycle shift, explains ~61% of this change |
| [[PANC-1 (line)]] | alt | 34.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | [[Bortezomib (drug)]] 0.05 µM 0.247× (z -10.8) ⚠ cell-cycle shift, explains ~61% of this change |
| [[SW 900 (line)]] | alt | 53.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | [[EX229 (drug)]] 5 µM 0.0238× (z -12.3) |
| [[SW48 (line)]] | wt | 35.3 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0617× (z -12.2) ⚠ cell-cycle shift, explains ~97% of this change |
| [[AsPC-1 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 24.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.176× (z -8.8) ⚠ cell-cycle shift, explains ~61% of this change |
| [[HS-578T (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 25.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.151× (z -8.6) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H1792 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 30.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 71.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.185× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +15.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 18.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +11.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 39.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -8.9) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SW1417 (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.314× (z -8.5) ⚠ cell-cycle shift, explains ~61% of this change |
| [[AN3 CA (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CKAP2]] | +0.94 | +0.93 / +0.94 | both halves | 7e-06 | STRING 781 |
| [[CCNB2]] | +0.93 | +0.93 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 902 |
| [[DLGAP5]] | +0.93 | +0.91 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 963 |
| [[KIF20A]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | STRING 948 |
| [[TOP2A]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 928 |
| [[CCNA2]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 943 |
| [[NUF2]] | +0.89 | +0.86 / +0.89 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 952 |
| [[CDKN3]] | +0.89 | +0.84 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 722 |
| [[KIF18A]] | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | same gene group; pathway: Mitotic Prometaphase; STRING 868 |
| [[BUB1]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 932 |
| [[PSRC1]] | +0.88 | +0.87 / +0.85 | both halves | 7e-06 |  |
| [[CENPE]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 834 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NEK2's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NEURL1B]] | B | NEURL1B activity raises NEK2's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without NEURL1B | 0.069 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PIMREG]] | B | PIMREG activity raises NEK2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.82× lower at baseline in the lines without PIMREG | 0.079 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.906). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.8, -57.3); signed map (-50.9, -42.3). **Vector** length 150, 52.7% of its response variance represented; |z| ≥ 3 in 1,377 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.70 to 46); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.71 to 41); *Mitotic Anaphase* (reactome, mean cos +0.71 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~84% of this change | +7.4 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.7 | +14.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +5.8 | +7.4 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +4.4 | +4.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +7.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.6 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +1.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -9.3 | -8.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | -9.2 | -8.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.6 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.2 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -5.1 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.5 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | NIMA related kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:211,658,657-211,675,630 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NLK1, NEK2A, RP67, PPP1R111 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; NIMA related kinase family |
| Hallmark sets | SPERMATOGENESIS, G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 32 pathways, smallest: APC-Cdc20 mediated degradation of Nek2A; GSK3B-mediated proteasomal degradation of PD-L1(CD274); APC:Cdc20 mediated degradation of cell cycle proteins prior to satisfation of the cell cycle checkpoint |
| Matched by | ensembl_id |

**Function**, from UniProt [P51955](https://www.uniprot.org/uniprotkb/P51955) (Serine/threonine-protein kinase Nek2):

> Protein kinase which is involved in the control of centrosome separation and bipolar spindle formation in mitotic cells and chromatin condensation in meiotic cells. Regulates centrosome separation (essential for the formation of bipolar spindles and high-fidelity chromosome separation) by phosphorylating centrosomal proteins such as CROCC, CEP250 and NINL, resulting in their displacement from the centrosomes. Regulates kinetochore microtubule attachment stability in mitosis via phosphorylation …

**Summary**, from NCBI Gene [4751](https://www.ncbi.nlm.nih.gov/gene/4751):

> This gene encodes a serine/threonine-protein kinase that is involved in mitotic regulation. This protein is localized to the centrosome, and undetectable during G1 phase, but accumulates progressively throughout the S phase, reaching maximal levels in late G2 phase. Alternatively spliced transcript variants encoding different isoforms with distinct C-termini have been noted for this gene. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:7745](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7745) · Entrez [4751](https://www.ncbi.nlm.nih.gov/gene/4751) · UniProt [P51955](https://www.uniprot.org/uniprotkb/P51955) · Ensembl [ENSG00000117650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117650)

## Data

Gene col 3939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3939); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3939]; `tensor/DDL_lfc|DDL_z.npy` [3939]; `embed/gene_vectors.npy` [3939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3939 or target_col == 3939). Every well: [[NEK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
