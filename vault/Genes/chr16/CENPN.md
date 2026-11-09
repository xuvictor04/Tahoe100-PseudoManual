---
symbol: "CENPN"
type: "gene"
col: 9310
ensembl_id: "ENSG00000166451"
name: "centromere protein N"
location: "16q23.2"
module: 6
arm: "+"
pooled_cpm: 34.33
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006", "written"]
generated_by: "tahoemap"
---

# CENPN

*centromere protein N* — 16q23.2

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> CENPN encodes CENP-N, the subunit of the constitutive centromere-associated network that reads the CENP-A nucleosome directly and so marks where a kinetochore is built.

## What it is

CENP-N was found in the complex that co-purifies with CENP-A chromatin, and is the component that recognises it specifically, contacting the CENP-A nucleosome through the histone's exposed RG loop. Structural work has since resolved that interface and shown how CENP-N bridges to CENP-L and sits alongside CENP-C in the inner kinetochore. Depleting it impairs kinetochore assembly and new CENP-A deposition, so cells lose chromosome segregation fidelity. Expression is proliferation-coupled rather than tissue-specific. Outside that structural role its literature is mostly correlative: raised expression in various tumours with survival associations, a weak basis for functional claims.

## What is uncertain

Nothing establishes CENPN as a p53 target in any direct sense, and in the earlier MG53/p53 study its membership of the p53 repression arm was only partially stable across cross-fitting folds, so it should be held more loosely than the core members of that arm. CENP-N's biology is executed at the protein level, so a fall in its transcript reports cells leaving the cycle, not a change in centromere function.

## References

- Foltz et al., 2006, Nature Cell Biology — defined the human CENP-A nucleosome-associated complex, including CENP-N.
- Carroll et al., 2009, Nature Cell Biology — showed CENP-N binds CENP-A nucleosomes directly and is required for centromere assembly.
- Chittori et al., 2018, Science — structural basis of centromeric nucleosome recognition by CENP-N.
- Engeland, 2018, Cell Death and Differentiation — review of p53-p21-DREAM-mediated repression of cell-cycle and mitosis genes.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.57× (z +14.0, q 6e-42, up in 35 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.71× (z +8.3, q 8e-15, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.523× (z -14.2, q 1e-42, down in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Rapamycin (drug)]] 0.5 µM: 0.790× (z -3.6, q 0.025, down in 16 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR62]] (+0.88, fdr 7e-06), [[MELK]] (+0.84, fdr 7e-06), [[POLQ]] (+0.84, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 22 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.57×** | +14.0 | 6e-42 | 35/38 (SW 900, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **2.44×** | +13.8 | 8e-41 | 42/44 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.03×** | +11.0 | 1e-25 | 44/46 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.98×** | +10.5 | 1e-23 | 43/47 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.83×** | +9.0 | 3e-17 | 37/46 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.74×** | +8.6 | 9e-16 | 37/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +8.3 | 8e-15 | 38/47 (PANC-1, A549, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.78×** | +8.2 | 1e-14 | 32/42 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.70×** | +8.2 | 2e-14 | 36/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.52×** | +6.2 | 3e-08 | 29/47 (A549, LoVo, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~81% of this change | **1.46×** | +5.8 | 3e-07 | 28/45 (SW1417, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.40×** | +5.2 | 1e-05 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.2 | 1e-05 | 27/46 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.24×** | +4.8 | 8e-05 | 22/47 (SW480, RKO, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.24×** | +4.8 | 8e-05 | 23/47 (HT-29, SW480, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.011 | 12/47 (HS-578T, SW1417, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.011 | 14/47 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.15× | +3.0 | 0.053 | 9/47 (HCT15, SW480, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.054 | 16/47 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.055 | 6/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +2.9 | 0.078 | 8/47 (SW480, KATO III, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.523×** | -14.2 | 1e-42 | 44/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.506×** | -10.5 | 2e-23 | 38/47 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.653×** | -6.6 | 8e-09 | 35/47 (Hs 766T, SW480, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.670×** | -4.4 | 0.001 | 22/47 (SW480, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.780×** | -3.8 | 0.014 | 18/47 (H4, SHP-77, …) | two highest doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.790×** | -3.6 | 0.025 | 16/47 (Hs 766T, A498, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.782×** | -3.6 | 0.028 | 15/47 (A-427, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -3.5 | 0.031 | 18/47 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.798×** | -3.5 | 0.031 | 20/46 (SW 900, H4, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.804×** | -3.4 | 0.038 | 19/47 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.738×** | -3.4 | 0.038 | 13/47 (SW480, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.661×** | -3.3 | 0.038 | 13/47 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.806×** | -3.1 | 0.071 | 12/47 (PANC-1, HCT15, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.810×** | -3.1 | 0.071 | 15/46 (A-427, SW480, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.868× | -3.1 | 0.072 | 16/47 (A-172, HCT15, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 71.9 | 4 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +12.1) ⚠ cell-cycle shift, explains ~64% of this change | [[Selinexor (drug)]] 5 µM 0.522× (z -10.1) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A498 (line)]] | wt | 51.6 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.285× (z -17.6) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.536× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 21.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | [[Selinexor (drug)]] 5 µM 0.400× (z -9.2) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 34.7 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.234× (z -14.2) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A-427 (line)]] | wt | 48.2 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.165× (z -21.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.413× (z -10.4) |
| [[H4 (line)]] | wt | 35.3 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.196× (z -11.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[KATO III (line)]] | alt | 36.1 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.39× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[LS 180 (line)]] | wt | 24.4 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0911× (z -14.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H2030 (line)]] | alt | 70.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.415× (z -11.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[PANC-1 (line)]] | alt | 29.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[SNU-423 (line)]] | alt | 26.0 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +8.7) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[SW 900 (line)]] | alt | 22.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.80× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[A549 (line)]] | wt | 24.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +11.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.321× (z -9.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[HOP62 (line)]] | alt | 43.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[Hs 766T (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.249× (z -8.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[LoVo (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.320× (z -8.8) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H1792 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[NCI-H23 (line)]] | alt | 43.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[NCI-H661 (line)]] | alt | 35.3 | 0 | 1 | — | [[Bicalutamide (drug)]] 0.5 µM 0.0695× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 24.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[AN3 CA (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.34 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR62]] | +0.88 | +0.88 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[MELK]] | +0.84 | +0.84 / +0.84 | both halves | 7e-06 | STRING 705 |
| [[POLQ]] | +0.84 | +0.85 / +0.84 | both halves | 7e-06 |  |
| [[SPC25]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 589 |
| [[FANCD2]] | +0.83 | +0.83 / +0.82 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.82 | +0.81 / +0.81 | both halves | 7e-06 | STRING 760 |
| [[KIF15]] | +0.82 | +0.79 / +0.83 | both halves | 7e-06 | STRING 614 |
| [[SKA3]] | +0.82 | +0.82 / +0.81 | both halves | 7e-06 | STRING 777 |
| [[PLK4]] | +0.81 | +0.84 / +0.79 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 600 |
| [[NCAPG2]] | +0.81 | +0.83 / +0.83 | both halves | 7e-06 | STRING 712 |
| [[CENPO]] | +0.81 | +0.83 / +0.80 | both halves | 7e-06 | same gene group; pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 999 |
| [[CENPK]] | +0.80 | +0.83 / +0.80 | both halves | 7e-06 | same gene group; pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises CENPN's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.1% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises CENPN's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.93× lower at baseline in the lines without E2F8 | 0.040 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises CENPN's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.75× lower at baseline in the lines without CDC25A | 0.076 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.812). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.7, -47.6); signed map (-40.8, -44.1). **Vector** length 111, 34.5% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.61 to 65); *DNA strand elongation* (reactome, mean cos +0.64 to 28); *DNA Replication* (reactome, mean cos +0.64 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +5.4 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +5.3 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | +4.8 | +8.2 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +3.2 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +3.2 | +8.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.9 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +8.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.4 | +3.5 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +2.1 | +2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | -0.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -10.0 | -14.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -8.7 | -10.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | -5.0 | -6.6 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -3.6 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein N |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.2 — chr16:81,006,552-81,033,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13607, FLJ22660, BM039; previously C16orf60 |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96H22](https://www.uniprot.org/uniprotkb/Q96H22) (Centromere protein N):

> Component of the CENPA-NAC (nucleosome-associated) complex, a complex that plays a central role in assembly of kinetochore proteins, mitotic progression and chromosome segregation. The CENPA-NAC complex recruits the CENPA-CAD (nucleosome distal) complex and may be involved in incorporation of newly synthesized CENPA into centromeres. CENPN is the first protein to bind specifically to CENPA nucleosomes and the direct binding of CENPA nucleosomes by CENPN is required for centromere assembly. …

**Summary**, from NCBI Gene [55839](https://www.ncbi.nlm.nih.gov/gene/55839):

> The protein encoded by this gene forms part of the nucleosome-associated complex and is important for kinetochore assembly. It is bound to kinetochores during S phase and G2 and recruits other proteins to the centromere. Pseudogenes of this gene are located on chromosome 2. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:30873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30873) · Entrez [55839](https://www.ncbi.nlm.nih.gov/gene/55839) · UniProt [Q96H22](https://www.uniprot.org/uniprotkb/Q96H22) · Ensembl [ENSG00000166451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166451)

## Data

Gene col 9310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9310); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9310]; `tensor/DDL_lfc|DDL_z.npy` [9310]; `embed/gene_vectors.npy` [9310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9310 or target_col == 9310). Every well: [[CENPN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/CENPN.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
