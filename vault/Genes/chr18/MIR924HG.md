---
symbol: "MIR924HG"
type: "gene"
col: 15548
ensembl_id: "ENSG00000267374"
name: "MIR924 host gene"
location: "18q12.2-q12.3"
module: 6
arm: "+"
pooled_cpm: 116.88
n_lines_expressing: 42
n_dd_up: 22
n_dd_down: 50
n_dd_up_clean: 13
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/006", "written"]
generated_by: "tahoemap"
---

# MIR924HG

*MIR924 host gene* — 18q12.2-q12.3

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> MIR924HG is a long non-coding RNA on chromosome 18, named for the microRNA encoded within it, and almost nothing about it is established.

## What it is

The gene is an annotation and a coordinate. Also catalogued as LINC00669, it is an intergenic non-coding transcript on chromosome 18 whose only named feature is that it hosts miR-924. Reference databases list no molecular function and no pathway membership. A single report in nasopharyngeal carcinoma proposes a pro-proliferative role acting on SOCS1; I cannot vouch for its details, and it has no evident replication. Whether the host transcript does anything of its own, rather than serving as the precursor from which miR-924 is excised, has not been addressed.

## What is uncertain

Essentially everything about the biology — though not, for once, the size of the measurement. This transcript is detected across almost the whole panel and at a level well above most obscure genes, so the detection floor and ambient RNA are not the worry here. What the reads *mean* is. A microRNA host transcript is cleaved as part of its own processing, so a count assigned to this locus mixes whatever mature host lncRNA exists with the unprocessed pri-miR-924 it is excised from, and a 3′-biased assay cannot separate the two — "MIR924HG expression" may be a readout of miR-924 production rather than of a lncRNA at all. With no established function there is no mechanism against which its assignment to the p53 repression arm in the earlier MG53/p53 study could be checked, and nothing separates real p53-dependent repression from depth and ambient-RNA covariates.

## References

No primary literature I can cite with confidence.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Cytarabine (drug)]] 5 µM: 1.58× (z +5.5, q 2e-05, up in 29 of 40 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Cytarabine (hydrochloride) (drug)]] 0.05 µM: 1.44× (z +4.2, q 0.002, up in 22 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.280× (z -22.0, q 0e+00, down in 37 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRIP1]] (+0.87, fdr 7e-06), [[POLQ]] (+0.86, fdr 7e-06), [[DTL]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[THSD4-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15548.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.58×** | +5.5 | 2e-05 | 29/40 (HT-29, RKO, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.53×** | +5.3 | 4e-05 | 29/40 (HT-29, HOP62, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.46×** | +4.7 | 5e-04 | 28/40 (HT-29, RKO, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.30×** | +4.6 | 5e-04 | 24/40 (A549, HT-29, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.30×** | +4.6 | 5e-04 | 23/40 (NCI-H2347, SNU-1, …) | top dose only | position effect removed |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.43×** | +4.4 | 8e-04 | 24/40 (SW48, NCI-H1573, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.44×** | +4.2 | 0.002 | 22/40 (HT-29, LS 180, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.42×** | +4.2 | 0.002 | 24/40 (HT-29, SNU-423, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.38×** | +4.0 | 0.003 | 21/40 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.008 | 18/40 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.010 | 17/41 (C-33 A, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.34×** | +3.6 | 0.013 | 20/40 (HOP62, Panc 03.27, …) | inconsistent across doses |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.013 | 17/40 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.21×** | +3.3 | 0.040 | 11/41 (HT-29, SNU-1, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.045 | 15/40 (BT-474, SNU-1, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.057 | 13/40 (LS 180, J82, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.073 | 13/40 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.084 | 14/40 (A-172, LS 180, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.084 | 15/40 (HT-29, SNU-423, …) | two highest doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.084 | 13/40 (LS 180, SW48, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.27×** | +2.9 | 0.090 | 11/41 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.18× | +2.9 | 0.091 | 11/40 (SHP-77, AsPC-1, …) | top dose only | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.18× | +2.9 | 0.091 | 8/40 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.26×** | +2.9 | 0.099 | 15/41 (LS 180, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15548.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.280×** | -22.0 | 0e+00 | 37/40 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.333×** | -13.6 | 1e-39 | 39/40 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.450×** | -9.5 | 4e-19 | 28/40 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -9.4 | 9e-19 | 28/41 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.241×** | -9.2 | 4e-18 | 35/41 (SHP-77, HCT15, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.616×** | -8.4 | 6e-15 | 26/40 (SNU-1, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.499×** | -8.3 | 1e-14 | 31/39 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.293×** | -7.9 | 1e-13 | 36/40 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.536×** | -7.7 | 7e-13 | 29/40 (A-172, LS 180, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.553×** | -6.9 | 2e-10 | 28/40 (LS 180, HCT15, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.457×** | -6.9 | 2e-10 | 29/40 (HT-29, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.682×** | -6.6 | 2e-09 | 31/41 (SHP-77, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.587×** | -6.6 | 2e-09 | 27/40 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.609×** | -6.1 | 4e-08 | 27/40 (A-427, SW48, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.613×** | -6.1 | 5e-08 | 33/41 (RKO, SW48, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.633×** | -5.7 | 6e-07 | 25/40 (SW48, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.658×** | -5.2 | 7e-06 | 23/40 (SHP-77, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.671×** | -4.9 | 2e-05 | 26/40 (Panc 03.27, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.08 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 237 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -19.5) |
| [[LS 180 (line)]] | wt | 225 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -18.5) |
| [[SW48 (line)]] | wt | 343 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -14.7) |
| [[A-172 (line)]] | wt | 255 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -12.8) |
| [[HCT15 (line)]] | alt | 536 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -18.1) |
| [[SHP-77 (line)]] | alt | 588 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -16.9) |
| [[J82 (line)]] | alt | 199 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -13.7) |
| [[PANC-1 (line)]] | alt | 118 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -15.4) |
| [[SNU-1 (line)]] | wt | 191 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0361× (z -18.2) |
| [[SW480 (line)]] | alt | 238 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -22.2) |
| [[H4 (line)]] | wt | 102 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 63.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -15.3) |
| [[A498 (line)]] | wt | 40.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 123 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 102 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -18.6) |
| [[COLO 205 (line)]] | alt | 149 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -19.3) |
| [[HOP62 (line)]] | alt | 227 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0694× (z -24.3) |
| [[LoVo (line)]] | wt | 79.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.6) |
| [[RKO (line)]] | wt | 319 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0917× (z -10.3) |
| [[AN3 CA (line)]] | alt | 165 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0498× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.7) |
| [[C-33 A (line)]] | alt | 168 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -9.6) |
| [[Hs 766T (line)]] | wt | 56.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.9) |
| [[HT-29 (line)]] | alt | 80.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 48.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.5) |
| [[SW1417 (line)]] | alt | 133 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.223× (z -11.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.0) |
| [[A549 (line)]] | wt | 64.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 60.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 77.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 53.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.460× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 100 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 50.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -12.0) |
| [[SW 1088 (line)]] | alt | 139 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0984× (z -8.7) |
| [[SW 1271 (line)]] | alt | 155 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.14 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 27.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.27 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRIP1]] | +0.87 | +0.82 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[POLQ]] | +0.86 | +0.86 / +0.84 | both halves | 7e-06 |  |
| [[DTL]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 |  |
| [[MELK]] | +0.84 | +0.85 / +0.81 | both halves | 7e-06 |  |
| [[FANCI]] | +0.84 | +0.86 / +0.81 | both halves | 7e-06 |  |
| [[EXO1]] | +0.84 | +0.82 / +0.82 | both halves | 7e-06 |  |
| [[WDHD1]] | +0.83 | +0.81 / +0.83 | both halves | 7e-06 |  |
| [[ATAD2]] | +0.82 | +0.81 / +0.79 | both halves | 7e-06 |  |
| [[CENPK]] | +0.82 | +0.85 / +0.80 | both halves | 7e-06 |  |
| [[WDR76]] | +0.81 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[GINS1]] | +0.81 | +0.82 / +0.79 | both halves | 7e-06 |  |
| [[BARD1]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THSD4-AS1]] | B | MIR924HG activity lowers THSD4-AS1's level | lines that do not express MIR924HG (8) vs lines expressing it (42) | 1.49× higher at baseline in the lines without MIR924HG | 0.045 | ⚠ within organs, on part of the lines; also absent: MIR193BHG |
| [[RTTN]] | B | MIR924HG activity lowers RTTN's level | lines that do not express MIR924HG (8) vs lines expressing it (42) | 1.61× higher at baseline in the lines without MIR924HG | 0.086 | ⚠ within organs, on part of the lines; also absent: MIR193BHG |
| [[FANCA]] | B | MIR924HG activity lowers FANCA's level | lines that do not express MIR924HG (8) vs lines expressing it (42) | 1.25× higher at baseline in the lines without MIR924HG | 0.087 | ⚠ within organs, on part of the lines; also absent: MIR193BHG |
| [[LIN54]] | B | MIR924HG activity raises LIN54's level | lines that do not express MIR924HG (8) vs lines expressing it (42) | 1.21× lower at baseline in the lines without MIR924HG | 0.089 | ⚠ within organs, on part of the lines; also absent: MIR193BHG |
| [[HMGB1P5]] | B | MIR924HG activity lowers HMGB1P5's level | lines that do not express MIR924HG (8) vs lines expressing it (42) | 1.21× higher at baseline in the lines without MIR924HG | 0.094 | ⚠ within organs, on part of the lines; also absent: MIR193BHG |
| [[RFWD3]] | B | MIR924HG activity lowers RFWD3's level | lines that do not express MIR924HG (8) vs lines expressing it (42) | 1.30× higher at baseline in the lines without MIR924HG | 0.094 | ⚠ within organs, on part of the lines; also absent: MIR193BHG |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.842). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.1, -46.6); signed map (-39.6, -44.2). **Vector** length 148, 51.4% of its response variance represented; |z| ≥ 3 in 1,492 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.62 to 65); *DNA strand elongation* (reactome, mean cos +0.66 to 28); *DNA Replication* (reactome, mean cos +0.66 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -1.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.7 | +3.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.7 | +4.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.9 | +3.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.9 | +2.9 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.8 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.3 | -13.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.0 | -8.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.6 | -6.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.6 | -7.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.9 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -6.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.5 | -4.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.3 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | MIR924 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18q12.2-q12.3 — chr18:39,206,917-39,800,322 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC00669 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44332) · Entrez [647946](https://www.ncbi.nlm.nih.gov/gene/647946) · Ensembl [ENSG00000267374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267374)

## Data

Gene col 15548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15548); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15548]; `tensor/DDL_lfc|DDL_z.npy` [15548]; `embed/gene_vectors.npy` [15548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15548 or target_col == 15548). Every well: [[MIR924HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/MIR924HG.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
