---
symbol: "PPM1D"
type: "gene"
col: 10009
ensembl_id: "ENSG00000170836"
name: "protein phosphatase, Mg2+/Mn2+ dependent 1D"
location: "17q23.3"
module: 62
arm: "+"
pooled_cpm: 61.73
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 16
n_dd_up_clean: 12
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# PPM1D

*protein phosphatase, Mg2+/Mn2+ dependent 1D* — 17q23.3

> [!summary] In one line
> PPM1D encodes WIP1, a p53-induced phosphatase that switches the DNA-damage response back off by stripping the activating phosphorylations off ATM, CHK1, CHK2, p53 and MDM2.

## What it is

WIP1 — wild-type p53-induced phosphatase 1 — is a Mg²⁺/Mn²⁺-dependent serine/threonine phosphatase of the PP2C family, encoded at 17q23.2. PP2C enzymes are monomeric — no regulatory or targeting subunits — so substrate choice is built into the catalytic domain rather than supplied by a partner. It was found as a transcript induced after ionising radiation in a p53-dependent manner, still the cleanest fact about it.

Its function is to reverse the damage response. The phosphorylations that ATM and ATR install to raise the alarm — ATM's own Ser1981 autophosphorylation, CHK2 Thr68, CHK1, Ser15 on p53, Ser139 on H2AX, Ser395 on MDM2, Thr180 on p38 MAPK — are WIP1 substrates. Because p53 drives PPM1D transcription and WIP1 then dephosphorylates p53 and its upstream kinases, the arrangement is a delayed negative feedback loop built one layer below [[MDM2]]'s: MDM2 controls how much p53 protein there is, WIP1 controls how activated it is. They converge: dephosphorylated MDM2 is more stable and binds p53 more avidly, so WIP1 reinforces the brake it parallels.

Clinically PPM1D behaves as an oncogene in tumours that keep wild-type p53: it sits in a recurrent 17q23 amplicon in breast cancer, where amplification was argued to abrogate p53 function without mutating it. A second, stranger mode came later: truncating mutations in the last two exons produce a stable protein that keeps the catalytic domain and behaves as gain-of-function. Acquired somatically in blood, they drive clonal haematopoiesis that expands specifically under cytotoxic chemotherapy; arising de novo in the germline, the same class of variant causes Jansen-de Vries syndrome. An allosteric inhibitor, GSK2830371, made the enzyme a tractable target.

## What is uncertain

The substrate list is long and mostly from overexpression and in vitro work. Which substrates WIP1 governs at endogenous levels in a given cell type is far less settled than the catalogue suggests, and papers differ on whether ATM, p53 or p38 is limiting. That PPM1D is a direct p53 target is well supported; whether its phosphatase activity is itself regulated — rather than simply set by how much protein is present — is not resolved, and no activating modification or ligand is established. The oncogenic mechanism is contested between a p53-centred route and a p38/p16-centred one. The 17q23 amplicon is broad and contains other candidate drivers, so amplification data alone do not pin a phenotype on PPM1D. Finally, the truncating variants show two distinct disease mechanisms pointing the same functional way; treating "PPM1D activity" as one quantity is a simplification.

## References

- Fiscella et al., 1997, PNAS — identified Wip1 as a human protein phosphatase induced by ionising radiation in a p53-dependent manner.
- Bulavin et al., 2002, Nature Genetics — amplification of PPM1D in human tumours abrogates p53 tumour-suppressor activity; Li et al. reported its oncogenic properties in the 17q23 breast cancer amplicon in the same journal and year.
- Shreeram et al., 2006, Molecular Cell — Wip1 modulates ATM-dependent signalling, including dephosphorylation of ATM Ser1981.
- Lu et al., 2007, Cancer Cell — Wip1 as a gatekeeper in the p53–MDM2 autoregulatory loop, acting through MDM2 stabilisation.
- Jansen et al., 2017, American Journal of Human Genetics — de novo truncating mutations in the last and penultimate exons of PPM1D cause an intellectual disability syndrome.
- Hsu et al., 2018, Cell Stem Cell — PPM1D mutations drive clonal haematopoiesis in response to cytotoxic chemotherapy.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.20× (z +15.8, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.430× (z -11.9, q 6e-30, down in 38 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.692× (z -5.2, q 3e-05, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRA2]] (+0.76, fdr 7e-06), [[DDB2]] (+0.74, fdr 7e-06), [[POLH]] (+0.73, fdr 7e-06); moves opposite to [[NUDC]] (-0.60, fdr 1e-05), [[CCT3]] (-0.59, fdr 1e-05), [[CCT5]] (-0.59, fdr 8e-06).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[GRIN2C]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MDM2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10009.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +15.8 | 0e+00 | 45/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.88×** | +14.9 | 0e+00 | 45/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.06×** | +12.0 | 9e-31 | 47/49 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +11.6 | 3e-29 | 41/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +10.3 | 9e-23 | 40/49 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.01×** | +9.9 | 5e-21 | 40/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.96×** | +9.5 | 1e-19 | 42/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +8.6 | 7e-16 | 39/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +8.1 | 4e-14 | 37/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +7.6 | 2e-12 | 35/47 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.71×** | +7.4 | 1e-11 | 37/48 (LOX-IMVI, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.65×** | +7.1 | 8e-11 | 32/48 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.54×** | +6.1 | 5e-08 | 31/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +5.1 | 1e-05 | 26/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.43×** | +5.1 | 1e-05 | 27/47 (NCI-H460, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 2e-04 | 23/47 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 2e-04 | 27/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Amsacrine (drug)]] 5 µM |  | 1.18× | +3.4 | 0.019 | 18/48 (C32, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10009.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.430×** | -11.9 | 6e-30 | 38/47 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.419×** | -11.8 | 9e-30 | 38/42 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.589×** | -7.5 | 1e-11 | 42/48 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.692×** | -5.2 | 3e-05 | 32/48 (NCI-H460, LoVo, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.549×** | -4.4 | 0.001 | 29/48 (NCI-H2347, A549, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.730×** | -4.3 | 0.002 | 28/48 (NCI-H1573, LoVo, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.568×** | -4.2 | 0.002 | 30/47 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.596×** | -3.8 | 0.009 | 25/48 (SW480, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.603×** | -3.7 | 0.012 | 23/48 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.780×** | -3.5 | 0.026 | 22/48 (A549, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **0.789×** | -3.3 | 0.045 | 19/47 (SW 1271, hTERT-HPNE, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.644×** | -3.2 | 0.055 | 21/46 (NCI-H1792, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.796×** | -3.2 | 0.058 | 14/48 (LS 180, J82, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.803×** | -3.1 | 0.079 | 19/49 (A-172, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.792×** | -3.0 | 0.088 | 20/45 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.807×** | -3.0 | 0.089 | 13/48 (LS 180, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10009. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 77.3 | 9 (4 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 63.0 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +15.0) | — |
| [[KATO III (line)]] | alt | 54.9 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.04× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.0656× (z -24.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +16.6) | — |
| [[A-427 (line)]] | wt | 115 | 4 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.4× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.0691× (z -24.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 75.2 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -16.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 161 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +13.9) | — |
| [[LS 180 (line)]] | wt | 93.9 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -12.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 39.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +17.2) | — |
| [[NCI-H23 (line)]] | alt | 40.3 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 91.7 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 39.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 82.8 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 19.3× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 60.2 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -13.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 66.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.30× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 28.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 50.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.0928× (z -18.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 50.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 51.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.6) | — |
| [[SW48 (line)]] | wt | 67.0 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 6.60× (z +10.3) | — |
| [[A549 (line)]] | wt | 134 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.90× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 37.3 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.99× (z +12.0) | — |
| [[C-33 A (line)]] | alt | 81.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -15.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 45.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +15.0) | — |
| [[CHP-212 (line)]] | wt | 299 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0290× (z -17.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 43.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 57.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -13.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 41.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 47.0 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.19× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 42.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 54.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -11.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 91.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +12.8) | — |
| [[C32 (line)]] | wt | 84.3 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 21.4× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 40.2 | 0 | 1 | — | [[LJI308 (drug)]] 5 µM 0.0696× (z -8.6) |
| [[HOP62 (line)]] | alt | 39.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 90.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -8.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 77.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 14.1× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 44.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 104 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10009), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRA2]] | +0.76 | +0.68 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[DDB2]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 456 |
| [[POLH]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[FDXR]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[SESN1]] | +0.71 | +0.61 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 452 |
| [[RPS27L]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[TP53INP1]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[POMZP3]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[PHPT1]] | +0.65 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ZMAT3]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 425 |
| [[GPX1]] | +0.64 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[PURPL]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDC]] | -0.60 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[CCT3]] | -0.59 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[CCT5]] | -0.59 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[STIP1]] | -0.57 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[CCT2]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[EIPR1]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[CHCHD3]] | -0.53 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[CCT6A]] | -0.53 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[PUM3]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[GNPNAT1]] | -0.52 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[HSPD1]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[UTP11]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIN2C]] | B | GRIN2C activity raises PPM1D's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.75× lower at baseline in the lines without GRIN2C | 0.005 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[PTCHD4]] | B | PTCHD4 activity raises PPM1D's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.72× lower at baseline in the lines without PTCHD4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[PINCR]] | B | PINCR activity raises PPM1D's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without PINCR | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[CYFIP2]] | B | CYFIP2 activity raises PPM1D's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.01× lower at baseline in the lines without CYFIP2 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[PURPL]] | B | PURPL activity raises PPM1D's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.55× lower at baseline in the lines without PURPL | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[BTG2]] | B | BTG2 activity raises PPM1D's level | lines that do not express BTG2 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without BTG2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CYFIP2, SLC37A1; maybe low, not absent |
| [[EDA2R]] | B | EDA2R activity raises PPM1D's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.44× lower at baseline in the lines without EDA2R | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MDM2]] | C | PPM1D's natural level strengthens MDM2's drug response | PPM1D's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.15; direction not clear | 0.092 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.1, 36.2); signed map (41.6, -24.9). **Vector** length 107, 36.0% of its response variance represented; |z| ≥ 3 in 1,448 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 targets up* (control, mean cos +0.57 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.53 to 6); *apoptosis* (hallmark, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +9.2 | +7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.9 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +10.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.3 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +1.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.3 | +0.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.7 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.2 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.6 | -4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.3 | +0.5 |
|  | [[EX229 (drug)]] 5 µM |  | -5.1 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase, Mg2+/Mn2+ dependent 1D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:60,600,193-60,666,280 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Wip1, PP2C-DELTA |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Hallmark sets | P53_PATHWAY, E2F_TARGETS |
| Reactome | 1 pathways, smallest: Transcriptional regulation by RUNX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O15297](https://www.uniprot.org/uniprotkb/O15297) (Protein phosphatase 1D):

> Involved in the negative regulation of p53 expression. Required for the relief of p53-dependent checkpoint mediated cell cycle arrest. Binds to and dephosphorylates 'Ser-15' of TP53 and 'Ser-345' of CHEK1 which contributes to the functional inactivation of these proteins. Mediates MAPK14 dephosphorylation and inactivation. Is also an important regulator of global heterochromatin silencing and critical in maintaining genome integrity (By similarity).

**Summary**, from NCBI Gene [8493](https://www.ncbi.nlm.nih.gov/gene/8493):

> The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. The expression of this gene is induced in a p53-dependent manner in response to various environmental stresses. While being induced by tumor suppressor protein TP53/p53, this phosphatase negatively regulates the activity of p38 MAP kinase, MAPK/p38, through which it reduces the phosphorylation of p53, and in …

**Accessions** — [HGNC:9277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9277) · Entrez [8493](https://www.ncbi.nlm.nih.gov/gene/8493) · UniProt [O15297](https://www.uniprot.org/uniprotkb/O15297) · Ensembl [ENSG00000170836](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170836)

## Data

Gene col 10009: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10009); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10009, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10009]; `tensor/DDL_lfc|DDL_z.npy` [10009]; `embed/gene_vectors.npy` [10009]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10009 or target_col == 10009). Every well: [[PPM1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/PPM1D.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
