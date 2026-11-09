---
symbol: "NPIPB5"
type: "gene"
col: 14374
ensembl_id: "ENSG00000243716"
name: "nuclear pore complex interacting protein family member B5"
location: "16p12.2"
module: 65
arm: "-"
pooled_cpm: 8.81
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# NPIPB5

*nuclear pore complex interacting protein family member B5* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.33× (z +10.4, q 1e-22, up in 37 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +8.3, q 4e-14, up in 28 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.589× (z -5.5, q 3e-05, down in 21 of 37 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.758× (z -4.2, q 0.007, down in 14 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (J82 0.161×, A498 0.185×, NCI-H1573 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (PANC-1 0.0355×, MIA PaCa-2 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1573 0.0894×, SK-MEL-2 0.103×; ⚠ toxic); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0637×); [[Vismodegib (drug)]] 0.5 µM in 1 line (C-33 A 0.0791×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.106×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPIPB4]] (+0.89, fdr 7e-06), [[PAK2]] (+0.60, fdr 1e-05), [[NUTM2B-AS1]] (+0.59, fdr 1e-05); moves opposite to [[FAM104A]] (-0.63, fdr 1e-05), [[WRAP53]] (-0.63, fdr 1e-05), [[FAM168A]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.33×** | +10.4 | 1e-22 | 37/48 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +8.3 | 4e-14 | 28/43 (COLO 205, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +4.7 | 5e-04 | 16/46 (SW 900, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.0 | 0.006 | 9/38 (J82, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.006 | 11/46 (NCI-H460, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.009 | 13/47 (COLO 205, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +3.2 | 0.100 | 12/47 (A498, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14374.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (J82 0.161×, A498 0.185×, NCI-H1573 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (PANC-1 0.0355×, MIA PaCa-2 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1573 0.0894×, SK-MEL-2 0.103×; ⚠ toxic); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0637×); [[Vismodegib (drug)]] 0.5 µM in 1 line (C-33 A 0.0791×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.106×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.589×** | -5.5 | 3e-05 | 21/37 (NCI-H1573, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.758×** | -4.2 | 0.007 | 14/47 (RKO, HT-29, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.695×** | -3.9 | 0.014 | 14/35 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.686×** | -3.9 | 0.014 | 9/16 (PANC-1, AsPC-1, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.699×** | -3.8 | 0.014 | 17/34 (J82, A498, …) | rises with dose | composition shift; position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.606×** | -3.5 | 0.037 | 10/43 (LS 180, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.638× | -3.2 | 0.12 | 10/43 (A498, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0894× (z -12.4) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 6.18 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.106× (z -8.9) |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0355× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[A498 (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[C-33 A (line)]] | alt | 9.27 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0791× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 4.32 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0637× (z -9.9) |
| [[J82 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.103× (z -9.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*27 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB4]] | +0.89 | +0.84 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[PAK2]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[NUTM2B-AS1]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ANKLE2]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[GSPT1]] | +0.55 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[DOCK1]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[NPIPB12]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ANAPC7]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[MTHFD1L]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[SPON1-AS1]] | +0.52 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[EIF3A]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CDV3]] | +0.52 | +0.50 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*73 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM104A]] | -0.63 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[WRAP53]] | -0.63 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[FAM168A]] | -0.63 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[DUSP11]] | -0.62 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[CNOT8]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[METTL17]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[MED6]] | -0.59 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[SNAPC3]] | -0.59 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[ZNF230]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[FAM8A1]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[PRMT9]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[LMBRD1]] | -0.57 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (6.8, -12.8); signed map (9.7, -8.3). **Vector** length 50.0, 6.13% of its response variance represented; |z| ≥ 3 in 856 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.9 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.7 | +8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +1.7 | +4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +1.5 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.4 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +0.9 | +1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.9 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +0.9 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.7 | -5.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.5 | -3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.3 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | nuclear pore complex interacting protein family member B5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:22,479,121-22,536,535 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [A8MRT5](https://www.uniprot.org/uniprotkb/A8MRT5) carries no function annotation.

**Summary**, from NCBI Gene [100132247](https://www.ncbi.nlm.nih.gov/gene/100132247):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:37233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37233) · Entrez [100132247](https://www.ncbi.nlm.nih.gov/gene/100132247) · UniProt [A8MRT5](https://www.uniprot.org/uniprotkb/A8MRT5) · Ensembl [ENSG00000243716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243716)

## Data

Gene col 14374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14374); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14374]; `tensor/DDL_lfc|DDL_z.npy` [14374]; `embed/gene_vectors.npy` [14374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14374 or target_col == 14374). Every well: [[NPIPB5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPIPB5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
