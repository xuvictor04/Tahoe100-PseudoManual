---
symbol: "USP7"
type: "gene"
col: 11922
ensembl_id: "ENSG00000187555"
name: "ubiquitin specific peptidase 7"
location: "16p13.2"
module: 3
arm: "-"
pooled_cpm: 126.31
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003", "written"]
generated_by: "tahoemap"
---

# USP7

*ubiquitin specific peptidase 7* — 16p13.2

> [!summary] In one line
> USP7 is the deubiquitinase that removes ubiquitin from both p53 and MDM2, which means its net effect on p53 depends on how much USP7 there is — the clearest case in the pathway of a regulator whose direction is not a fixed property.

## What it is

USP7, long known as HAUSP (herpesvirus-associated ubiquitin-specific protease), has an N-terminal TRAF-like domain, a catalytic USP domain, and C-terminal ubiquitin-like domains that fold back to activate it. The TRAF-like domain carries the substrate-binding pocket, which p53 and MDM2 bind through similar short motifs — as does EBNA1 of Epstein–Barr virus, which is how the enzyme got its name.

Its relationship to p53 is the textbook case of a non-monotonic regulator. USP7 deubiquitinates p53 and stabilises it, even against excess MDM2, which predicts that losing USP7 should destabilise p53. Disrupting the gene in human cells did the opposite: p53 was stabilised and functionally activated. The resolution is that MDM2 is also a USP7 substrate and the more sensitive one — it needs deubiquitination to survive long enough to act as a ligase — so partial loss of USP7 lowers p53 while near-complete loss removes MDM2 first and raises it. Both behaviours have been reported in the same system at different knockdown depths.

Beyond p53 the substrate list is long — MDMX/[[MDM4]], PTEN, Claspin, FOXO4, Tip60, UHRF1 — and germline variants cause Hao-Fountain syndrome. Selective inhibitors reported in 2017 act through the MDM2 arm: they destabilise MDM2, raise p53 and induce targets including [[CDKN1A]].

## What is uncertain

"USP7 stabilises p53" is an incomplete statement, and any experiment reading out p53 after changing USP7 must report the depth of the perturbation before its sign can be interpreted. How much of the inhibitors' anti-tumour effect runs through p53 rather than other substrates is actively argued, and it matters clinically: the non-p53 substrates would predict activity in TP53-mutant tumours. Much of the substrate list derives from overexpression or immunoprecipitation work, and the weight of individual entries is uneven. For this dataset, USP7 mRNA is close to uninformative about USP7 activity — the enzyme is allosterically activated by its own C-terminal tail, competed for by abundant substrates, and present in excess of what the p53 axis consumes.

## References

- Li et al., 2002, *Nature* — showed HAUSP deubiquitinates p53 and stabilises it even in the presence of excess MDM2.
- Cummins et al., 2004, *Nature* — disrupting the HAUSP gene in human cells stabilised and activated p53, the opposite of the predicted result.
- Li et al., 2004, *Molecular Cell* — partial reduction of HAUSP destabilised p53 while near-complete loss stabilised it, giving the dose-dependent model.
- Saridakis et al., 2005, *Molecular Cell* — structural basis for EBNA1 and p53 competing for the same USP7 binding site.
- Turnbull et al., 2017, *Nature* — FT671 and FT827 inhibit USP7 selectively, destabilising MDM2, raising p53 and inducing p21.
- Kategaya et al., 2017, *Nature* — independent small-molecule USP7 inhibitors acting by interfering with ubiquitin binding.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.03× (z +25.6, q 0e+00, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.06× (z +18.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.406× (z -23.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TASOR]] (+0.72, fdr 1e-05), [[CYREN]] (+0.70, fdr 1e-05), [[CPSF2]] (+0.65, fdr 3e-05); moves opposite to [[B3GAT3]] (-0.63, fdr 2e-05), [[COX6A1]] (-0.61, fdr 2e-05), [[GUK1]] (-0.60, fdr 4e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11922.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.03×** | +25.6 | 0e+00 | 45/48 (HOP62, A498, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.06×** | +18.6 | 0e+00 | 46/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +14.6 | 0e+00 | 45/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.97×** | +14.6 | 0e+00 | 48/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +12.8 | 2e-35 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +12.3 | 5e-33 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +12.3 | 1e-32 | 42/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +12.1 | 1e-31 | 40/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +11.9 | 1e-30 | 45/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.23×** | +10.7 | 4e-25 | 43/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +9.5 | 1e-19 | 41/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +8.5 | 9e-16 | 40/48 (HT-29, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +7.6 | 2e-12 | 35/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +6.8 | 5e-10 | 34/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +5.5 | 1e-06 | 25/48 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 2e-04 | 24/49 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.12× | +4.2 | 7e-04 | 3/48 (H4, RKO, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.015 | 19/48 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.019 | 11/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11922.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.406×** | -23.1 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.412×** | -22.7 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.520×** | -16.8 | 0e+00 | 47/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.747×** | -7.2 | 1e-10 | 33/47 (SW1417, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.746×** | -6.8 | 9e-10 | 38/48 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.876× | -4.8 | 1e-04 | 10/48 (A498, CHP-212, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 0.876× | -4.8 | 1e-04 | 17/48 (CHP-212, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.882× | -4.6 | 4e-04 | 15/49 (RKO, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.833×** | -4.5 | 4e-04 | 23/47 (NCI-H23, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.746×** | -3.9 | 0.005 | 22/49 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.858× | -3.9 | 0.005 | 14/47 (NCI-H23, Panc 03.27, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.855× | -3.9 | 0.005 | 20/48 (SW480, AN3 CA, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.900× | -3.8 | 0.006 | 15/48 (A-172, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.866× | -3.7 | 0.009 | 22/48 (KATO III, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.873× | -3.5 | 0.019 | 13/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.912× | -3.1 | 0.063 | 3/49 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.912× | -3.1 | 0.063 | 4/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.884× | -3.1 | 0.065 | 8/49 (NCI-H23, RKO, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11922. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 98.5 | 12 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +19.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.92× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.412× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 152 | 10 (3 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +17.1) | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.488× (z -9.8) |
| [[SW480 (line)]] | alt | 159 | 9 (3 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.306× (z -21.9) |
| [[AsPC-1 (line)]] | alt | 231 | 7 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +21.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.328× (z -16.2) |
| [[PANC-1 (line)]] | alt | 151 | 8 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +18.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +17.0) | [[Panobinostat (drug)]] 5 µM 0.389× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 110 | 6 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +19.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.87× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.375× (z -14.6) |
| [[LoVo (line)]] | wt | 137 | 7 (3 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +19.7) | [[Panobinostat (drug)]] 5 µM 0.354× (z -18.1) |
| [[KATO III (line)]] | alt | 161 | 5 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +17.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.260× (z -21.9) |
| [[LS 180 (line)]] | wt | 149 | 5 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.372× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 98.2 | 7 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.403× (z -10.9) |
| [[HT-29 (line)]] | alt | 105 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +12.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.16× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.378× (z -15.3) |
| [[Panc 03.27 (line)]] | alt | 87.5 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +18.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.35× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.319× (z -14.2) |
| [[A549 (line)]] | wt | 133 | 4 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +19.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.99× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -14.5) |
| [[HepG2_C3A (line)]] | wt | 163 | 4 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.43× (z +9.7) | [[Belinostat (drug)]] 5 µM 0.422× (z -10.8) |
| [[HOP62 (line)]] | alt | 90.4 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +22.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.74× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.322× (z -16.3) |
| [[SW48 (line)]] | wt | 154 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 3.12× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -12.9) |
| [[COLO 205 (line)]] | alt | 105 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +14.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 182 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.285× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 138 | 3 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.376× (z -12.6) |
| [[RKO (line)]] | wt | 167 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.9) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -14.2) |
| [[SW1417 (line)]] | alt | 163 | 2 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +14.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.382× (z -15.1) |
| [[A-427 (line)]] | wt | 135 | 2 (1 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.14× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.486× (z -11.1) |
| [[A498 (line)]] | wt | 126 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +22.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.354× (z -14.0) |
| [[BT-474 (line)]] | alt | 128 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -14.1) |
| [[HS-578T (line)]] | alt | 94.3 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +19.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.435× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 96.9 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +14.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.36× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.383× (z -10.7) |
| [[A-172 (line)]] | wt | 131 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.429× (z -11.5) |
| [[C-33 A (line)]] | alt | 231 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.456× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 93.8 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +18.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.454× (z -9.2) |
| [[H4 (line)]] | wt | 111 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.55× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 65.8 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +16.7) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.370× (z -13.2) |
| [[SNU-423 (line)]] | alt | 85.2 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +17.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.06× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.483× (z -9.5) |
| [[Hs 766T (line)]] | wt | 110 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.17× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.407× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 116 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.89× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.384× (z -10.6) |
| [[J82 (line)]] | alt | 126 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.376× (z -14.1) |
| [[RPMI-7951 (line)]] | alt | 102 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.62× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -10.6) |
| [[SW 900 (line)]] | alt | 91.6 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.9) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.426× (z -9.7) |
| [[C32 (line)]] | wt | 95.1 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 6.66× (z +10.8) | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.262× (z -8.6) |
| [[HCT15 (line)]] | alt | 152 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.472× (z -9.1) |
| [[AN3 CA (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -24.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 103 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.103× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 132 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11922), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | +0.72 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[CYREN]] | +0.70 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CPSF2]] | +0.65 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[C9orf64]] | +0.65 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[UTP20]] | +0.64 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CUL1]] | +0.63 | +0.50 / +0.47 | both halves | 2e-05 | STRING 609 |
| [[DNAJC11]] | +0.62 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[COX18]] | +0.62 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ZFP91]] | +0.61 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[UBE3A]] | +0.61 | +0.48 / +0.54 | both halves | 2e-05 | STRING 496 |
| [[AFG1L]] | +0.61 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[ZNF507]] | +0.61 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GAT3]] | -0.63 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[COX6A1]] | -0.61 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[GUK1]] | -0.60 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[CASP9]] | -0.60 | -0.42 / -0.38 | both halves | 6e-05 | pathway: Intracellular signaling by second messengers |
| [[CBFA2T2]] | -0.60 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[KCTD7]] | -0.57 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[SDHAP2]] | -0.56 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ADIPOR1]] | -0.56 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[ANAPC11]] | -0.56 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[SDHAP1]] | -0.55 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[EDF1]] | -0.55 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[UBL5]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises USP7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-5.2, 2.0); signed map (16.5, -26.8). **Vector** length 70.8, 19.9% of its response variance represented; |z| ≥ 3 in 1,402 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +8.4 | +25.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.0 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.3 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +5.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | -2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.8 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.7 | -16.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -22.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | +12.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.1 | +12.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -23.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | +3.0 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.4 | +1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | +2.4 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.3 | +0.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.2 — chr16:8,892,097-8,975,328 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HAUSP |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 18 pathways, smallest: Regulation of PTEN localization; Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Regulation of TP53 Degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93009](https://www.uniprot.org/uniprotkb/Q93009) (Ubiquitin C-terminal hydrolase 7):

> Hydrolase that deubiquitinates target proteins such as ARMC5, FOXO4, DEPTOR, KAT5, p53/TP53, MDM2, ERCC6, DNMT1, UHRF1, PTEN, KMT2E/MLL5 and DAXX. Together with DAXX, prevents MDM2 self-ubiquitination and enhances the E3 ligase activity of MDM2 towards p53/TP53, thereby promoting p53/TP53 ubiquitination and proteasomal degradation. Deubiquitinates p53/TP53, preventing degradation of p53/TP53, and enhances p53/TP53-dependent transcription regulation, cell growth repression and apoptosis. …

**Summary**, from NCBI Gene [7874](https://www.ncbi.nlm.nih.gov/gene/7874):

> The protein encoded by this gene belongs to the peptidase C19 family, which includes ubiquitinyl hydrolases. This protein deubiquitinates target proteins such as p53 (a tumor suppressor protein) and WASH (essential for endosomal protein recycling), and regulates their activities by counteracting the opposing ubiquitin ligase activity of proteins such as HDM2 and TRIM27, involved in the respective process. Mutations in this gene have been implicated in a neurodevelopmental disorder. [provided by …

**Accessions** — [HGNC:12630](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12630) · Entrez [7874](https://www.ncbi.nlm.nih.gov/gene/7874) · UniProt [Q93009](https://www.uniprot.org/uniprotkb/Q93009) · Ensembl [ENSG00000187555](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187555)

## Data

Gene col 11922: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11922); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11922, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11922]; `tensor/DDL_lfc|DDL_z.npy` [11922]; `embed/gene_vectors.npy` [11922]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11922 or target_col == 11922). Every well: [[USP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/USP7.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
