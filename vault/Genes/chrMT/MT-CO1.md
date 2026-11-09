---
symbol: "MT-CO1"
type: "gene"
col: 12684
ensembl_id: "ENSG00000198804"
name: "mitochondrially encoded cytochrome c oxidase I"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 758.27
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-CO1

*mitochondrially encoded cytochrome c oxidase I* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.09× (z +12.8, q 1e-34, up in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Palmatine (chloride) (drug)]] 5 µM: 1.27× (z +4.0, q 0.009, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.221× (z -16.6, q 0e+00, down in 48 of 48 measured lines) ⚠ transcription drop. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.499× (z -11.6, q 2e-28, down in 45 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12684.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.09×** | +12.8 | 1e-34 | 43/44 (LoVo, A549, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.11×** | +12.4 | 8e-33 | 45/45 (A549, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.16×** | +11.1 | 2e-26 | 49/49 (NCI-H1573, A549, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.5 | 0.001 | 39/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.009 | 29/48 (SNU-423, SW1417, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.018 | 31/48 (NCI-H2347, HepG2/C3A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.4 | 0.051 | 28/38 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.051 | 32/48 (C32, NCI-H1792, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | 1.30× | +3.1 | 0.12 | 39/48 (Hs 766T, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12684.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.221×** | -16.6 | 0e+00 | 48/48 (SK-MEL-2, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.499×** | -11.6 | 2e-28 | 45/48 (NCI-H460, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.396×** | -10.9 | 2e-25 | 42/48 (Hs 766T, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.463×** | -9.1 | 2e-17 | 43/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.588×** | -8.8 | 1e-16 | 43/49 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.480×** | -8.6 | 5e-16 | 43/48 (BT-474, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.493×** | -8.3 | 7e-15 | 40/48 (BT-474, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 5 µM |  | **0.653×** | -5.0 | 4e-05 | 47/48 (J82, A498, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.662×** | -4.9 | 7e-05 | 37/48 (SW480, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **0.719×** | -3.7 | 0.011 | 40/48 (SHP-77, Hs 766T, …) | top dose only | plate-row cell shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.632×** | -3.6 | 0.017 | 47/48 (BT-474, SNU-423, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Berbamine (drug)]] 5 µM |  | **0.807×** | -3.6 | 0.017 | 31/49 (SHP-77, C32, …) | top dose only | position effect removed |
| [[Infigratinib (drug)]] 0.5 µM |  | **0.659×** | -3.5 | 0.021 | 44/49 (NCI-H23, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Methotrexate (drug)]] 5 µM |  | **0.746×** | -3.4 | 0.024 | 45/48 (KATO III, SNU-1, …) | top dose only | position effect removed |
| [[venetoclax (drug)]] 0.5 µM |  | **0.679×** | -3.2 | 0.042 | 41/49 (PANC-1, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | **0.823×** | -3.2 | 0.042 | 33/49 (PANC-1, SHP-77, …) | top dose only | position effect removed |
| [[Ciclopirox (drug)]] 5 µM |  | **0.826×** | -3.2 | 0.049 | 26/48 (SW480, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 799 | 3 (3 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.61× (z +12.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.168× (z -16.8) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 962 | 3 (3 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.43× (z +12.3) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.232× (z -22.3) |
| [[HOP62 (line)]] | alt | 461 | 4 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Palmatine (chloride) (drug)]] 5 µM 2.21× (z +10.3) | [[Pentamidine (isethionate) (drug)]] 5 µM 0.326× (z -14.6) |
| [[SW 900 (line)]] | alt | 677 | 3 (3 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.34× (z +10.3) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.308× (z -15.5) |
| [[Hs 766T (line)]] | wt | 972 | 1 (1 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.54× (z +9.0) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.273× (z -18.9) |
| [[LoVo (line)]] | wt | 952 | 3 (3 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.05× (z +12.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.174× (z -15.7) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 737 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.41× (z +12.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.312× (z -18.2) |
| [[SW1417 (line)]] | alt | 702 | 4 (3 ⚠) | 4 (1 ⚠) | [[Palmatine (chloride) (drug)]] 5 µM 2.09× (z +11.4) | [[Docetaxel (drug)]] 0.05 µM 0.180× (z -17.4) ⚠ transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.503× (z -10.5) |
| [[C-33 A (line)]] | alt | 552 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.74× (z +10.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.197× (z -13.2) ⚠ transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.429× (z -10.4) |
| [[LS 180 (line)]] | wt | 768 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.11× (z +9.4) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -15.9) |
| [[PANC-1 (line)]] | alt | 836 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.18× (z +11.0) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.247× (z -19.4) |
| [[SHP-77 (line)]] | alt | 1,383 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.91× (z +10.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.156× (z -18.7) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -11.4) |
| [[SNU-1 (line)]] | wt | 863 | 0 | 7 (2 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.254× (z -18.5) |
| [[A-427 (line)]] | wt | 690 | 2 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.93× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Palmatine (chloride) (drug)]] 5 µM 1.84× (z +8.6) | [[Pentamidine (isethionate) (drug)]] 5 µM 0.305× (z -16.6) |
| [[A498 (line)]] | wt | 979 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.52× (z +12.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.184× (z -15.9) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.369× (z -14.2) |
| [[A549 (line)]] | wt | 943 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.65× (z +13.0) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.348× (z -16.2) |
| [[BT-474 (line)]] | alt | 1,518 | 1 | 5 (2 ⚠) | [[Palmatine (chloride) (drug)]] 5 µM 1.75× (z +9.1) | [[Docetaxel (drug)]] 0.05 µM 0.155× (z -19.8) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -16.2) |
| [[C32 (line)]] | wt | 598 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.09× (z +10.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.253× (z -12.1) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.434× (z -11.1) |
| [[H4 (line)]] | wt | 449 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +11.0) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.311× (z -13.1) |
| [[hTERT-HPNE (line)]] | wt | 466 | 4 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.73× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Palmatine (chloride) (drug)]] 5 µM 2.14× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.315× (z -9.9) |
| [[KATO III (line)]] | alt | 1,249 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.80× (z +10.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.163× (z -17.1) ⚠ transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.388× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 577 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.95× (z +12.1) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.215× (z -19.8) |
| [[NCI-H2030 (line)]] | alt | 897 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.57× (z +11.4) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.301× (z -16.3) |
| [[RKO (line)]] | wt | 735 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.88× (z +8.9) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 666 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.41× (z +11.7) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.271× (z -12.1) ⚠ transcription drop |
| [[CFPAC-1 (line)]] | alt | 584 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.00× (z +10.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.304× (z -11.8) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.522× (z -9.7) |
| [[HS-578T (line)]] | alt | 423 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 3.81× (z +10.7) ⚠ toxic; transcription drop | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.352× (z -12.7) |
| [[HT-29 (line)]] | alt | 640 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.18× (z +10.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.225× (z -12.6) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.353× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 359 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +9.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.303× (z -14.3) |
| [[SNU-423 (line)]] | alt | 627 | 4 (3 ⚠) | 1 (1 ⚠) | [[Palmatine (chloride) (drug)]] 5 µM 2.40× (z +12.4) | [[Docetaxel (drug)]] 0.05 µM 0.258× (z -12.4) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 686 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.79× (z +10.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.218× (z -11.9) ⚠ transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.465× (z -9.0) |
| [[HCT15 (line)]] | alt | 427 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.07× (z +12.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.280× (z -9.3) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 863 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.04× (z +12.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.234× (z -12.5) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 566 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.09× (z +11.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.264× (z -11.4) ⚠ transcription drop |
| [[NCI-H2347 (line)]] | alt | 548 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.03× (z +10.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.204× (z -15.4) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 568 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.87× (z +11.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.227× (z -12.4) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 371 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.97× (z +9.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.431× (z -9.1) |
| [[COLO 205 (line)]] | alt | 891 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.125× (z -17.6) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 737 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.90× (z +8.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.418× (z -10.8) |
| [[J82 (line)]] | alt | 569 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.75× (z +9.7) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.217× (z -14.2) ⚠ transcription drop |
| [[NCI-H23 (line)]] | alt | 1,017 | 0 | 3 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.129× (z -17.5) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.313× (z -15.0) |
| [[NCI-H661 (line)]] | alt | 834 | 0 | 3 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.187× (z -11.1) ⚠ transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.280× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 490 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.23× (z +9.9) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.379× (z -8.8) |
| [[SW48 (line)]] | wt | 880 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.05× (z +10.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.233× (z -12.9) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 1,108 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.21× (z +10.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.111× (z -20.8) ⚠ transcription drop |
| [[CHP-212 (line)]] | wt | 608 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.236× (z -9.8) ⚠ transcription drop |
| [[SW 1271 (line)]] | alt | 375 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.337× (z -9.5) |
| [[NCI-H2122 (line)]] | alt | 755 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 798 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 649 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | mitochondrially encoded cytochrome c oxidase I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:5,904-7,445 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COX1, COI; previously MTCO1 |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits; Mitochondrially encoded protein coding genes |
| Reactome | 23 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; tRNA processing in the mitochondrion; Mitochondrial mRNA modification |
| Matched by | ensembl_id |

**Function**, from UniProt [P00395](https://www.uniprot.org/uniprotkb/P00395) (Cytochrome c oxidase subunit 1):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [4512](https://www.ncbi.nlm.nih.gov/gene/4512):

> Contributes to cytochrome-c oxidase activity. Predicted to be involved in aerobic respiration; positive regulation of vasoconstriction; and respiratory electron transport chain. Located in mitochondrial membrane. Part of respiratory chain complex IV. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7419) · Entrez [4512](https://www.ncbi.nlm.nih.gov/gene/4512) · UniProt [P00395](https://www.uniprot.org/uniprotkb/P00395) · Ensembl [ENSG00000198804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198804)

## Data

Gene col 12684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12684); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12684, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12684]; `tensor/DDL_lfc|DDL_z.npy` [12684]; `embed/gene_vectors.npy` [12684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12684 or target_col == 12684). Every well: [[MT-CO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-CO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
