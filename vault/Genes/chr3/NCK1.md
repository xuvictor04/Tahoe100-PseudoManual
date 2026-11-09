---
symbol: "NCK1"
type: "gene"
col: 8131
ensembl_id: "ENSG00000158092"
name: "NCK adaptor protein 1"
location: "3q22.3"
module: 49
arm: "+"
pooled_cpm: 101.64
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# NCK1

*NCK adaptor protein 1* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.73× (z +10.2, q 2e-21, up in 45 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 10 lines (SW480 5.08×, COLO 205 10.1×, KATO III 4.99×, HT-29 5.54×, …).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.363× (z -19.6, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.603× (z -13.6, q 5e-40, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GORASP2]] (+0.73, fdr 7e-06), [[MYPOP]] (+0.72, fdr 7e-06), [[PRRC1]] (+0.72, fdr 7e-06); moves opposite to [[DDX5]] (-0.70, fdr 7e-06), [[EIF4G2]] (-0.65, fdr 1e-05), [[MMADHC-DT]] (-0.64, fdr 1e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8131.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 10 lines (SW480 5.08×, COLO 205 10.1×, KATO III 4.99×, HT-29 5.54×, …).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.73×** | +10.2 | 2e-21 | 45/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.5 | 1e-05 | 0/50 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.27×** | +4.6 | 7e-04 | 31/49 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.15 | 14/49 (HEC-1-A, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8131.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.363×** | -19.6 | 0e+00 | 48/49 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.354×** | -19.3 | 0e+00 | 41/44 (NCI-H1573, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -13.6 | 5e-40 | 44/49 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.495×** | -12.6 | 3e-34 | 42/45 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.630×** | -12.4 | 4e-33 | 37/48 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.633×** | -8.5 | 2e-15 | 36/48 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.738×** | -8.2 | 1e-14 | 41/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.696×** | -6.7 | 1e-09 | 39/50 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.715×** | -6.5 | 5e-09 | 34/48 (SNU-423, HCT15, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.708×** | -6.4 | 7e-09 | 35/48 (HS-578T, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.758×** | -5.4 | 4e-06 | 31/48 (HS-578T, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.773×** | -5.0 | 3e-05 | 26/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.816×** | -3.9 | 0.003 | 25/48 (HT-29, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.816×** | -3.9 | 0.003 | 27/48 (LOX-IMVI, SW 1088, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.805×** | -3.9 | 0.004 | 25/47 (LS 180, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.821×** | -3.8 | 0.005 | 22/48 (KATO III, Hs 766T, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.717×** | -3.4 | 0.022 | 20/47 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.850× | -3.2 | 0.039 | 11/49 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.850× | -3.1 | 0.039 | 13/49 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Ritonavir (drug)]] 5 µM |  | 0.890× | -3.1 | 0.039 | 7/48 (RPMI-7951, HepG2/C3A, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.852× | -3.1 | 0.042 | 16/49 (HEC-1-A, Panc 03.27, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.853× | -3.0 | 0.065 | 18/48 (NCI-H1792, SW 1088, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.861× | -2.9 | 0.080 | 17/48 (NCI-H1573, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 144 | 1 | 9 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.91× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.427× (z -10.4) |
| [[HS-578T (line)]] | alt | 140 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -14.7) |
| [[HOP62 (line)]] | alt | 104 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.555× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 94.2 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -9.1) |
| [[SW1417 (line)]] | alt | 123 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.92× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -11.9) |
| [[A-172 (line)]] | wt | 92.1 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0790× (z -26.6) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.537× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 142 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -15.8) |
| [[SNU-423 (line)]] | alt | 86.5 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.400× (z -9.9) |
| [[A498 (line)]] | wt | 175 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -17.6) |
| [[BT-474 (line)]] | alt | 85.5 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.51× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -16.7) |
| [[KATO III (line)]] | alt | 135 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.99× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.313× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 135 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -23.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -14.3) |
| [[C32 (line)]] | wt | 83.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 82.0 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 155 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -12.0) |
| [[SW480 (line)]] | alt | 98.3 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.08× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -13.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 91.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 93.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -20.1) |
| [[C-33 A (line)]] | alt | 86.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0981× (z -20.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 150 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0861× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 95.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 85.2 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.276× (z -10.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 123 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.96× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -19.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 82.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -10.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 96.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -12.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 79.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -8.8) |
| [[A-427 (line)]] | wt | 112 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.34× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -11.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 95.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0671× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -8.6) |
| [[HT-29 (line)]] | alt | 69.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.54× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -10.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 77.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -9.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 71.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -8.6) |
| [[LS 180 (line)]] | wt | 70.7 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.29× (z +8.9) | [[Harringtonine (drug)]] 0.05 µM 0.393× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 77.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0880× (z -24.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 62.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0990× (z -18.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 88.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -15.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 91.3 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.198× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 85.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 70.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -9.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 73.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 80.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GORASP2]] | +0.73 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[MYPOP]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.72 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[USPL1]] | +0.72 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.71 | +0.76 / +0.50 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.70 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[AKR1A1]] | +0.70 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PRUNE1]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.69 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.69 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[RNF41]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.68 | +0.74 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.70 | -0.66 / -0.66 | both halves | 7e-06 |  |
| [[EIF4G2]] | -0.65 | -0.54 / -0.58 | both halves | 1e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[MMADHC-DT]] | -0.64 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[ST7L]] | -0.63 | -0.68 / -0.39 | both halves | 5e-05 |  |
| [[PSMD6-AS1]] | -0.62 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[MSRA]] | -0.62 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ITPR2-AS1]] | -0.62 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[CYREN]] | -0.62 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[SSUH2]] | -0.62 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[CACNA2D1]] | -0.61 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[AKT1S1]] | -0.61 | -0.64 / -0.35 | both halves | 1e-04 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING |
| [[NEK10]] | -0.61 | -0.63 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NCK1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.3, -14.9); signed map (-36.1, -2.7). **Vector** length 103, 31.0% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +4.2 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +4.2 | +4.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +10.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +1.1 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.0 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -8.4 | -12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.0 | -8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -19.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -12.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -6.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.3 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -3.9 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | NCK adaptor protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:136,862,208-136,951,606 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NCKalpha; previously NCK |
| Gene groups (HGNC) | SH2 domain containing; SH3 domain containing |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, ALLOGRAFT_REJECTION, MITOTIC_SPINDLE |
| Reactome | 40 pathways, smallest: Activation of RAC1; DCC mediated attractive signaling; Generation of second messenger molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P16333](https://www.uniprot.org/uniprotkb/P16333) (SH2/SH3 adapter protein NCK1):

> Adapter protein which associates with tyrosine-phosphorylated growth factor receptors, such as KDR and PDGFRB, or their cellular substrates. Maintains low levels of EIF2S1 phosphorylation by promoting its dephosphorylation by PP1. Plays a role in the DNA damage response, not in the detection of the damage by ATM/ATR, but for efficient activation of downstream effectors, such as that of CHEK2. Plays a role in ELK1-dependent transcriptional activation in response to activated Ras signaling. …

**Summary**, from NCBI Gene [4690](https://www.ncbi.nlm.nih.gov/gene/4690):

> The protein encoded by this gene is one of the signaling and transforming proteins containing Src homology 2 and 3 (SH2 and SH3) domains. It is located in the cytoplasm and is an adaptor protein involved in transducing signals from receptor tyrosine kinases to downstream signal recipients such as RAS. Alternatively spliced transcript variants encoding different isoforms have been found. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:7664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7664) · Entrez [4690](https://www.ncbi.nlm.nih.gov/gene/4690) · UniProt [P16333](https://www.uniprot.org/uniprotkb/P16333) · Ensembl [ENSG00000158092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158092)

## Data

Gene col 8131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8131); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8131]; `tensor/DDL_lfc|DDL_z.npy` [8131]; `embed/gene_vectors.npy` [8131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8131 or target_col == 8131). Every well: [[NCK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
