---
symbol: "PTPRH"
type: "gene"
col: 1273
ensembl_id: "ENSG00000080031"
name: "protein tyrosine phosphatase receptor type H"
location: "19q13.42"
module: 189
arm: "+"
pooled_cpm: 37.41
n_lines_expressing: 44
n_dd_up: 7
n_dd_down: 41
n_dd_up_clean: 6
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# PTPRH

*protein tyrosine phosphatase receptor type H* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.62× (z +7.2, q 4e-10, up in 30 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.538× (z -13.2, q 7e-37, down in 31 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYT5]] (+0.65, fdr 1e-05, ⚠ read-through risk), [[CASP9]] (+0.62, fdr 3e-05), [[RDH13]] (+0.61, fdr 3e-05), [[DLGAP4]] (+0.60, fdr 1e-05); moves opposite to [[ECHDC1]] (-0.64, fdr 3e-05), [[ZNF618]] (-0.59, fdr 2e-05), [[TGFBRAP1]] (-0.57, fdr 2e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF618]] → it (grade B ⚠); 2 go from it, the strongest it → [[LINC00595]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.62×** | +7.2 | 4e-10 | 30/41 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.58×** | +7.1 | 5e-10 | 29/41 (NCI-H2030, SW480, …) | rises with dose | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.34×** | +6.2 | 1e-07 | 23/42 (LS 180, KATO III, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.66×** | +4.1 | 0.005 | 18/40 (COLO 205, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.009 | 16/42 (LoVo, KATO III, …) | top dose only |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.014 | 14/42 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[RMC-6236 (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.014 | 14/42 (AsPC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.11 | 11/42 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.23× | +3.1 | 0.11 | 14/42 (AsPC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.22× | +3.1 | 0.12 | 12/42 (HOP62, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 21 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1273.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.538×** | -13.2 | 7e-37 | 31/42 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.468×** | -11.3 | 3e-27 | 35/39 (HepG2/C3A, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.503×** | -10.6 | 4e-24 | 26/40 (HT-29, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.607×** | -10.4 | 4e-23 | 32/42 (C32, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.526×** | -9.6 | 1e-19 | 27/41 (A-172, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.520×** | -9.4 | 6e-19 | 28/36 (A-172, HT-29, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.546×** | -9.0 | 2e-17 | 33/41 (H4, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.583×** | -8.0 | 6e-14 | 27/40 (A-172, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.588×** | -7.9 | 2e-13 | 23/31 (NCI-H1792, A-172, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.596×** | -7.7 | 7e-13 | 33/42 (HT-29, A-172, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.616×** | -7.5 | 3e-12 | 28/41 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -7.0 | 1e-10 | 28/43 (CFPAC-1, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.733×** | -6.5 | 4e-09 | 22/41 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.671×** | -6.2 | 3e-08 | 25/41 (H4, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.671×** | -6.2 | 3e-08 | 23/42 (RPMI-7951, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.678×** | -6.0 | 7e-08 | 19/41 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.769×** | -5.6 | 8e-07 | 22/42 (A549, A-172, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.559×** | -4.7 | 6e-05 | 21/40 (HT-29, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.740×** | -4.7 | 7e-05 | 18/42 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.575×** | -4.5 | 2e-04 | 19/40 (COLO 205, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.575×** | -4.5 | 2e-04 | 19/41 (CFPAC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -4.4 | 2e-04 | 20/42 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.752×** | -4.3 | 4e-04 | 20/42 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.792×** | -3.6 | 0.005 | 16/42 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.799×** | -3.5 | 0.008 | 13/42 (NCI-H2347, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 157 | 0 | 16 (15 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -24.8) |
| [[A-172 (line)]] | wt | 61.2 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 72.8 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -14.6) |
| [[H4 (line)]] | wt | 38.0 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0364× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[MIA PaCa-2 (line)]] | alt | 55.2 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 55.9 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0409× (z -26.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -13.7) |
| [[A549 (line)]] | wt | 56.8 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 45.0 | 0 | 5 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -11.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.203× (z -10.8) |
| [[C32 (line)]] | wt | 30.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.287× (z -9.9) |
| [[Hs 766T (line)]] | wt | 53.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[HS-578T (line)]] | alt | 20.8 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 54.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 54.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 17.3 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -10.0) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 67.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -10.1) |
| [[SNU-1 (line)]] | wt | 54.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[A-427 (line)]] | wt | 21.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.43× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[HepG2_C3A (line)]] | wt | 83.3 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0688× (z -21.0) ⚠ toxic |
| [[J82 (line)]] | alt | 26.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.167× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[LoVo (line)]] | wt | 20.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.126× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 81.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.3) |
| [[LS 180 (line)]] | wt | 24.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 31.6 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.57× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[NCI-H2347 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 1 | — | [[NG25 (drug)]] 5 µM 0.0442× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -9.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[A498 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.07 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYT5]] | +0.65 | +0.52 / +0.63 | both halves | 1e-05 | ⚠ **readthrough risk**: SYT5 lies 1.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[CASP9]] | +0.62 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[RDH13]] | +0.61 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[DLGAP4]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[RELA]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[DNAAF3]] | +0.59 | +0.55 / +0.43 | both halves | 3e-05 | ⚠ **readthrough risk**: DNAAF3 lies 14.5 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[NBEAL1]] | +0.59 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[ARID5A]] | +0.59 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[LRRFIP1]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.58 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[SYP]] | +0.58 | +0.58 / +0.27 | both halves | 3e-04 |  |
| [[CCNYL1]] | +0.58 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[SPAG9]] | +0.57 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[STK40]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECHDC1]] | -0.64 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[ZNF618]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[TGFBRAP1]] | -0.57 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[USP13]] | -0.56 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[ITPKB]] | -0.56 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[GTF2I]] | -0.55 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[METAP1D]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ALDH5A1]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZZZ3]] | -0.54 | -0.37 / -0.56 | both halves | 7e-05 |  |
| [[KLHL42]] | -0.54 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[DHRS4L2]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SNX5]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF618]] | B | ZNF618 activity lowers PTPRH's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 3.29× higher at baseline in the lines without ZNF618 | 0.005 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[SYT5]] | B | SYT5 activity raises PTPRH's level | lines that do not express SYT5 (10) vs lines expressing it (40) | 3.40× lower at baseline in the lines without SYT5 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with EP300, RNF43, ACVR2A; also absent: B4GALNT1, LARP6; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises PTPRH's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00595]] | B | PTPRH activity lowers LINC00595's level | lines that do not express PTPRH (6) vs lines expressing it (44) | 1.51× higher at baseline in the lines without PTPRH | 0.068 | ⚠ within organs, on part of the lines; co-occurs with EP300, RNF43, ZFHX3; also absent: RAB32, PDE4A, ADAL |
| [[RING1]] | B | PTPRH activity lowers RING1's level | lines that do not express PTPRH (6) vs lines expressing it (44) | 1.17× higher at baseline in the lines without PTPRH | 0.071 | ⚠ within organs, on part of the lines; co-occurs with EP300, RNF43, ZFHX3; also absent: RAB32, PDE4A, ADAL |

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.9, -0.7); signed map (-19.2, 24.9). **Vector** length 104, 27.8% of its response variance represented; |z| ≥ 3 in 1,283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.4 | -2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.6 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +5.0 | +7.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.9 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | +4.6 | -10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +4.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.6 | -10.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -2.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,181,247-55,209,506 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SAP-1 |
| Gene groups (HGNC) | Fibronectin type III domain containing; Protein tyrosine phosphatases receptor type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HD43](https://www.uniprot.org/uniprotkb/Q9HD43) (Receptor-type tyrosine-protein phosphatase H):

> Protein phosphatase that may contribute to contact inhibition of cell growth and motility by mediating the dephosphorylation of focal adhesion-associated substrates and thus negatively regulating integrin-promoted signaling processes. Induces apoptotic cell death by at least two distinct mechanisms: inhibition of cell survival signaling mediated by PI 3-kinase, Akt, and ILK and activation of a caspase-dependent pro-apoptotic pathway. Inhibits the basal activity of LCK and its activation in …

**Summary**, from NCBI Gene [5794](https://www.ncbi.nlm.nih.gov/gene/5794):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region, a single transmembrane region, and a single intracytoplasmic catalytic domain, and thus represents a receptor-type PTP. The extracellular region contains eight fibronectin type III-like …

**Accessions** — [HGNC:9672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9672) · Entrez [5794](https://www.ncbi.nlm.nih.gov/gene/5794) · UniProt [Q9HD43](https://www.uniprot.org/uniprotkb/Q9HD43) · Ensembl [ENSG00000080031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080031)

## Data

Gene col 1273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1273); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1273]; `tensor/DDL_lfc|DDL_z.npy` [1273]; `embed/gene_vectors.npy` [1273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1273 or target_col == 1273). Every well: [[PTPRH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
