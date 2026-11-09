---
symbol: "ARID5A"
type: "gene"
col: 12292
ensembl_id: "ENSG00000196843"
name: "AT-rich interaction domain 5A"
location: "2q11.2"
module: 189
arm: "+"
pooled_cpm: 13.75
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 39
n_dd_up_clean: 9
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# ARID5A

*AT-rich interaction domain 5A* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.59× (z +12.3, q 3e-32, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.502× (z -8.9, q 3e-16, down in 31 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.578× (z -7.1, q 2e-10, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMC1]] (+0.64, fdr 4e-05), [[THEMIS2]] (+0.62, fdr 1e-05), [[ENO2]] (+0.61, fdr 1e-05); moves opposite to [[FOXG1]] (-0.54, fdr 4e-04), [[PRDX6-AS1]] (-0.53, fdr 3e-05), [[NDUFS1]] (-0.52, fdr 7e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[C15orf48]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Panobinostat (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.59×** | +12.3 | 3e-32 | 42/47 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.46×** | +11.7 | 5e-29 | 37/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.11×** | +9.7 | 8e-20 | 33/46 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.81×** | +7.4 | 2e-11 | 31/44 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.66×** | +6.6 | 4e-09 | 30/45 (SK-MEL-2, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +3.9 | 0.008 | 16/46 (SHP-77, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.027 | 13/46 (HT-29, SHP-77, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.031 | 9/45 (COLO 205, SHP-77, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.040 | 11/46 (RPMI-7951, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.045 | 12/47 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +3.3 | 0.050 | 14/47 (NCI-H460, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12292.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.502×** | -8.9 | 3e-16 | 31/36 (A-172, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.525×** | -8.0 | 4e-13 | 20/28 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.572×** | -7.2 | 1e-10 | 26/42 (LS 180, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.578×** | -7.1 | 2e-10 | 23/45 (C-33 A, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.578×** | -7.1 | 2e-10 | 26/47 (HEC-1-A, LS 180, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -6.6 | 5e-09 | 23/44 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.589×** | -6.3 | 2e-08 | 22/33 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -6.0 | 1e-07 | 24/40 (BT-474, A-172, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -5.6 | 1e-06 | 22/42 (SK-MEL-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.636×** | -5.6 | 1e-06 | 20/46 (NCI-H23, RPMI-7951, …) | rises with dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.645×** | -5.1 | 2e-05 | 22/45 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -4.5 | 3e-04 | 17/44 (SNU-423, SW 900, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.718×** | -4.1 | 0.002 | 16/45 (LOX-IMVI, Hs 766T, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.718×** | -4.1 | 0.002 | 16/45 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.806×** | -3.9 | 0.003 | 16/46 (NCI-H1792, NCI-H1573, …) | rises with dose | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.738×** | -3.9 | 0.003 | 15/45 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.806×** | -3.9 | 0.003 | 18/47 (SNU-423, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.739×** | -3.9 | 0.003 | 16/45 (NCI-H1792, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.810×** | -3.8 | 0.004 | 14/46 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.728×** | -3.8 | 0.005 | 14/44 (SNU-423, NCI-H1792, …) | all doses, flat |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.815×** | -3.7 | 0.006 | 15/46 (SHP-77, NCI-H2347, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.750×** | -3.7 | 0.006 | 16/45 (NCI-H1792, NCI-H1573, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0539× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 52.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 25.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0415× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 16.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 15.2 | 0 | 2 (1 ⚠) | — | [[Budesonide (drug)]] 0.5 µM 0.0916× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 26.2 | 1 | 1 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.21× (z +8.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -11.1) |
| [[SW480 (line)]] | alt | 7.27 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.34× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.142× (z -8.5) ⚠ cell-cycle shift, explains ~53% of this change |
| [[CFPAC-1 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.168× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.158× (z -10.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 6.49 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.89× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 8.80 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0602× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 7.95 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0945× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-423 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0802× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMC1]] | +0.64 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[THEMIS2]] | +0.62 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ENO2]] | +0.61 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[TMOD1]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PTPRH]] | +0.59 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[PPP2R5B]] | +0.58 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[MFSD12]] | +0.57 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[IFFO2]] | +0.57 | +0.51 / +0.43 | both halves | 4e-05 |  |
| [[DLGAP4]] | +0.56 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[EHD4]] | +0.55 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[PIGA]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[RELA]] | +0.55 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXG1]] | -0.54 | -0.51 / -0.26 | both halves | 4e-04 |  |
| [[PRDX6-AS1]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[NDUFS1]] | -0.52 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[ECHDC1]] | -0.51 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[RPRD2]] | -0.51 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[COPS8-DT]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[SLC26A2]] | -0.51 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[MCCC2]] | -0.51 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[TFAM]] | -0.50 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[YAP1]] | -0.50 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[LINC01551]] | -0.50 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[ANGEL2]] | -0.50 | -0.44 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C15orf48]] | B | C15orf48 activity raises ARID5A's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 1.38× lower at baseline in the lines without C15orf48 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[MAF]] | B | MAF activity raises ARID5A's level | lines that do not express MAF (27) vs lines expressing it (23) | 1.67× lower at baseline in the lines without MAF | 0.020 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[MMP13]] | B | MMP13 activity raises ARID5A's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 1.37× lower at baseline in the lines without MMP13 | 0.031 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[TOP2A]] | B | TOP2A activity raises ARID5A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DTNA]] | B | DTNA activity raises ARID5A's level | lines that do not express DTNA (22) vs lines expressing it (28) | 1.52× lower at baseline in the lines without DTNA | 0.072 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |
| [[DUSP10]] | B | DUSP10 activity raises ARID5A's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 1.82× lower at baseline in the lines without DUSP10 | 0.073 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers ARID5A's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Panobinostat (drug)]] 0.5 µM | C | ARID5A's natural level lowers the cells' numbers under Panobinostat 0.5 µM (makes them more sensitive) | ARID5A's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.75 | 0.162 over the table, 0.002 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.1, -1.8); signed map (-19.5, 26.4). **Vector** length 109, 26.3% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.1 | +11.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.1 | +12.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.6 | +9.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.3 | +7.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +3.5 |
| fall | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.7 | -5.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -4.2 | -7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.0 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.8 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | AT-rich interaction domain 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,536,743-96,552,634 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRF-1, RP11-363D14 |
| Gene groups (HGNC) | AT-rich interaction domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03989](https://www.uniprot.org/uniprotkb/Q03989) (AT-rich interactive domain-containing protein 5A):

> DNA-binding protein that may regulate transcription and act as a repressor by binding to AT-rich stretches in the promoter region of target genes. May positively regulate chondrocyte-specific transcription such as of COL2A1 in collaboration with SOX9 and positively regulate histone H3 acetylation at chondrocyte-specific genes. May stimulate early-stage chondrocyte differentiation and inhibit later stage differention (By similarity). Can repress ESR1-mediated transcriptional activation; proposed …

**Summary**, from NCBI Gene [10865](https://www.ncbi.nlm.nih.gov/gene/10865):

> Members of the ARID protein family, including ARID5A, have diverse functions but all appear to play important roles in development, tissue-specific gene expression, and regulation of cell growth (Patsialou et al., 2005 [PubMed 15640446]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17361) · Entrez [10865](https://www.ncbi.nlm.nih.gov/gene/10865) · UniProt [Q03989](https://www.uniprot.org/uniprotkb/Q03989) · Ensembl [ENSG00000196843](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196843)

## Data

Gene col 12292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12292); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12292]; `tensor/DDL_lfc|DDL_z.npy` [12292]; `embed/gene_vectors.npy` [12292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12292 or target_col == 12292). Every well: [[ARID5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARID5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
