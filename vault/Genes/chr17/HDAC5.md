---
symbol: "HDAC5"
type: "gene"
col: 3002
ensembl_id: "ENSG00000108840"
name: "histone deacetylase 5"
location: "17q21.31"
module: 74
arm: "+"
pooled_cpm: 52.7
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 38
n_dd_up_clean: 15
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# HDAC5

*histone deacetylase 5* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +12.7, q 6e-34, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (13 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.205× (z -25.6, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.513× (z -15.2, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2B]] (+0.76, fdr 7e-06), [[KLHL24]] (+0.70, fdr 7e-06), [[GPX4]] (+0.70, fdr 1e-05); moves opposite to [[ALG8]] (-0.68, fdr 7e-06), [[PIGW]] (-0.65, fdr 2e-05), [[TSR1]] (-0.64, fdr 7e-06).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[KLHL24]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +12.7 | 6e-34 | 40/48 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +10.7 | 3e-24 | 41/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +9.8 | 2e-20 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +8.5 | 2e-15 | 42/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +8.3 | 1e-14 | 38/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.49×** | +6.2 | 7e-08 | 34/47 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.34×** | +4.7 | 2e-04 | 32/49 (SW1417, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +4.6 | 3e-04 | 25/49 (LOX-IMVI, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.4 | 8e-04 | 22/48 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.001 | 25/47 (SK-MEL-2, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.002 | 25/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.002 | 23/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.007 | 21/50 (A-427, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.28×** | +3.7 | 0.009 | 20/50 (NCI-H596, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.7 | 0.009 | 19/48 (RPMI-7951, RKO, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.022 | 14/48 (SHP-77, BT-474, …) | all doses, stronger at high dose |  |
| [[MK-3903 (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.032 | 12/48 (NCI-H1573, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3002.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.205×** | -25.6 | 0e+00 | 47/48 (NCI-H2347, AsPC-1, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.513×** | -15.2 | 0e+00 | 44/49 (hTERT-HPNE, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.447×** | -13.0 | 3e-36 | 43/49 (SW48, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.213×** | -12.9 | 3e-36 | 48/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.240×** | -11.9 | 7e-31 | 46/48 (SK-MEL-2, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.241×** | -11.9 | 1e-30 | 47/48 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.474×** | -11.6 | 4e-29 | 32/42 (Panc 03.27, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.478×** | -11.0 | 3e-26 | 37/44 (SW 900, HT-29, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.269×** | -11.0 | 3e-26 | 45/48 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.333×** | -9.2 | 2e-18 | 43/48 (HEC-1-A, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.610×** | -7.6 | 1e-12 | 42/48 (NCI-H1792, C-33 A, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.427×** | -7.1 | 5e-11 | 38/46 (NCI-H661, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.634×** | -6.9 | 2e-10 | 35/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.753×** | -6.5 | 4e-09 | 28/48 (NCI-H460, AN3 CA, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.663×** | -6.4 | 7e-09 | 34/50 (NCI-H2347, C32, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.536×** | -6.3 | 9e-09 | 34/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.695×** | -5.5 | 1e-06 | 27/48 (SW 900, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.788×** | -5.4 | 2e-06 | 30/48 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.551×** | -5.0 | 2e-05 | 24/49 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.622×** | -4.8 | 4e-05 | 28/49 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.5 | 10 (4 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +15.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.101× (z -19.9) ⚠ unreliable plate only · without an alert: [[Selinexor (drug)]] 5 µM 0.379× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 76.5 | 0 | 12 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.108× (z -26.4) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 83.1 | 0 | 8 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.154× (z -17.8) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -11.7) |
| [[SW1417 (line)]] | alt | 47.6 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.251× (z -12.2) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 96.2 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -17.4) |
| [[HOP62 (line)]] | alt | 51.7 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.214× (z -14.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 1 (1 ⚠) | 5 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.56× (z +10.7) ⚠ position not correctable | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0890× (z -17.4) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -11.7) |
| [[A-172 (line)]] | wt | 50.1 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.313× (z -10.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -9.6) |
| [[A549 (line)]] | wt | 50.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0858× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.129× (z -9.3) |
| [[C32 (line)]] | wt | 40.6 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[LoVo (line)]] | wt | 43.0 | 2 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.241× (z -12.1) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.305× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 42.3 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.7) | [[EX229 (drug)]] 5 µM 0.0697× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 65.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0827× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -10.0) |
| [[SNU-423 (line)]] | alt | 75.4 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.201× (z -16.5) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -16.3) |
| [[SW 900 (line)]] | alt | 71.8 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 61.3 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.114× (z -19.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0985× (z -11.0) |
| [[HT-29 (line)]] | alt | 65.4 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.168× (z -17.4) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 63.2 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.171× (z -16.0) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 44.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -14.9) |
| [[RKO (line)]] | wt | 38.7 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +11.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.195× (z -10.2) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0513× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 81.5 | 2 | 2 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.07× (z +9.9) | [[c-Kit-IN-1 (drug)]] 5 µM 0.0141× (z -19.5) |
| [[AsPC-1 (line)]] | alt | 49.4 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0867× (z -20.1) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.3) |
| [[CHP-212 (line)]] | wt | 155 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 104 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.264× (z -11.3) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.9) |
| [[Hs 766T (line)]] | wt | 36.0 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.221× (z -11.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0895× (z -9.5) |
| [[HS-578T (line)]] | alt | 54.9 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.204× (z -14.1) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 32.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +13.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.204× (z -12.1) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 78.4 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.141× (z -15.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.125× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 47.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0638× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW48 (line)]] | wt | 67.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0473× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 30.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.195× (z -13.9) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 60.7 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.169× (z -13.6) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 54.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.227× (z -10.6) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 36.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +13.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.289× (z -9.0) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 52.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +13.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.113× (z -15.3) ⚠ unreliable plate only |
| [[NCI-H596 (line)]] | alt | 62.0 | 1 (1 ⚠) | 1 | [[Trametinib (drug)]] 5 µM 3.29× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | [[Methylthiouracil (drug)]] 5 µM 0.305× (z -8.8) |
| [[SNU-1 (line)]] | wt | 67.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW 1271 (line)]] | alt | 83.1 | 0 | 2 (1 ⚠) | — | [[Menadione (drug)]] 0.05 µM 0.0909× (z -9.5) |
| [[A-427 (line)]] | wt | 62.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -10.4) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 58.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.159× (z -8.5) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 53.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.251× (z -9.3) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 33.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.159× (z -9.0) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.205× (z -12.7) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 75.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.224× (z -11.7) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2B]] | +0.76 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[KLHL24]] | +0.70 | +0.68 / +0.82 | both halves | 7e-06 |  |
| [[GPX4]] | +0.70 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[TBC1D17]] | +0.69 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[WDR48]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[YPEL3]] | +0.68 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[PNPLA2]] | +0.67 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | +0.67 | +0.59 / +0.65 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CDKN2D]] | +0.67 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[MEF2D]] | +0.67 | +0.57 / +0.64 | both halves | 8e-06 | pathway: HALLMARK_MYOGENESIS; STRING 936 |
| [[CCDC28A]] | +0.66 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[CDKN1C]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[CBX7]] | +0.66 | +0.58 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG8]] | -0.68 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[PIGW]] | -0.65 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[TSR1]] | -0.64 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[DHX37]] | -0.64 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[DUS2]] | -0.64 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[NUP205]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[UTP20]] | -0.63 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.63 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[E2F3]] | -0.62 | -0.64 / -0.52 | both halves | 1e-05 | pathway: Signaling by NOTCH |
| [[ANAPC1]] | -0.62 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[PRMT3]] | -0.62 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[PRDM5]] | -0.62 | -0.46 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises HDAC5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NOVA2]] | B | NOVA2 activity lowers HDAC5's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.09× higher at baseline in the lines without NOVA2 | 0.087 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[YPEL2]] | C | YPEL2 activity raises HDAC5's level | lines that do not express YPEL2 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without YPEL2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL24]] | C | HDAC5's natural level strengthens KLHL24's drug response | HDAC5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.13; direction not clear | 0.069 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | HDAC5's natural level raises the cells' numbers under SBI-0640756 5 µM (protects the cells) | HDAC5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65 | 0.361 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.3, -47.4); signed map (-17.6, 10.0). **Vector** length 148, 51.3% of its response variance represented; |z| ≥ 3 in 1,536 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +8.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.9 | +10.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.2 | +9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +7.0 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.5 | +8.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.0 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +4.0 | +1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.9 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -17.5 | -25.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -11.1 | -12.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -10.6 | -11.9 |
|  | [[EX229 (drug)]] 5 µM |  | -10.2 | -11.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -10.1 | -11.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.6 | -9.2 |

## What is on record

|  |  |
|---|---|
| Name | histone deacetylase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,076,746-44,123,702 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0600, NY-CO-9, FLJ90614 |
| Gene groups (HGNC) | Histone deacetylases, class IIA |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING, MYOGENESIS |
| Reactome | 18 pathways, smallest: Notch-HLH transcription pathway; NOTCH signaling regulates gene expression in endothelial stalk cells; NOTCH1 Intracellular Domain Regulates Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQL6](https://www.uniprot.org/uniprotkb/Q9UQL6) (Histone deacetylase 5):

> In vitro, it deacetylates lysine residues on the N-terminal part of the core histones (H2A, H2B, H3 and H4). Histone deacetylation gives a tag for epigenetic repression and plays an important role in transcriptional regulation, cell cycle progression and developmental events. Histone deacetylases act via the formation of large multiprotein complexes. Involved in muscle maturation by repressing transcription of myocyte enhancer MEF2C. During muscle differentiation, it shuttles into the …

**Summary**, from NCBI Gene [10014](https://www.ncbi.nlm.nih.gov/gene/10014):

> Histones play a critical role in transcriptional regulation, cell cycle progression, and developmental events. Histone acetylation/deacetylation alters chromosome structure and affects transcription factor access to DNA. The protein encoded by this gene belongs to the class II histone deacetylase/acuc/apha family. It possesses histone deacetylase activity and represses transcription when tethered to a promoter. It coimmunoprecipitates only with HDAC3 family member and might form multicomplex …

**Accessions** — [HGNC:14068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14068) · Entrez [10014](https://www.ncbi.nlm.nih.gov/gene/10014) · UniProt [Q9UQL6](https://www.uniprot.org/uniprotkb/Q9UQL6) · Ensembl [ENSG00000108840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108840)

## Data

Gene col 3002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3002); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3002]; `tensor/DDL_lfc|DDL_z.npy` [3002]; `embed/gene_vectors.npy` [3002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3002 or target_col == 3002). Every well: [[HDAC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDAC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
