---
symbol: "RHOG"
type: "gene"
col: 10791
ensembl_id: "ENSG00000177105"
name: "ras homolog family member G"
location: "11p15.4"
module: 20
arm: "-"
pooled_cpm: 15.27
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RHOG

*ras homolog family member G* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.74× (z +6.9, q 3e-09, up in 25 of 46 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.72× (z +6.4, q 5e-08, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.700× (z -4.5, q 0.005, down in 15 of 23 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (HS-578T 0.101×, PANC-1 0.266×, NCI-H2030 0.143×, J82 0.254×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW1417 0.360×, LoVo 0.348×; ⚠ cell-cycle shift, explains ~89% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (AsPC-1 0.145×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.192×); [[Sodium Salicylate (drug)]] 0.5 µM in 1 line (SHP-77 0.0685×); [[Hesperidin (drug)]] 5 µM in 1 line (HepG2/C3A 0.103×).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKCD]] (+0.65, fdr 1e-05), [[ELOF1]] (+0.62, fdr 4e-05), [[MAP1S]] (+0.60, fdr 1e-04); moves opposite to [[HNRNPA3]] (-0.57, fdr 4e-04), [[PTGR2]] (-0.55, fdr 6e-05), [[EWSR1]] (-0.53, fdr 3e-04).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.74×** | +6.9 | 3e-09 | 25/46 (PANC-1, A549, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.72×** | +6.4 | 5e-08 | 27/47 (PANC-1, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.4 | 0.002 | 20/39 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.2 | 0.004 | 14/44 (SNU-423, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.22×** | +3.6 | 0.033 | 18/46 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.041 | 10/43 (SW480, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.043 | 7/47 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.051 | 6/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.3 | 0.052 | 0/48 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.29×** | +3.3 | 0.056 | 15/42 (CFPAC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.29×** | +3.2 | 0.056 | 15/45 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.056 | 11/47 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.058 | 12/41 (MIA PaCa-2, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10791.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (HS-578T 0.101×, PANC-1 0.266×, NCI-H2030 0.143×, J82 0.254×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW1417 0.360×, LoVo 0.348×; ⚠ cell-cycle shift, explains ~89% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (AsPC-1 0.145×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.192×); [[Sodium Salicylate (drug)]] 0.5 µM in 1 line (SHP-77 0.0685×); [[Hesperidin (drug)]] 5 µM in 1 line (HepG2/C3A 0.103×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.700×** | -4.5 | 0.005 | 15/23 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.750×** | -3.7 | 0.052 | 20/33 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Roxadustat (drug)]] 5 µM |  | 0.760× | -3.4 | 0.12 | 11/46 (NCI-H23, HOP62, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 31.8 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +23.1) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.39× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -12.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 30.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.2) ⚠ cell-cycle shift, explains ~89% of this change | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 33.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.1) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[NCI-H460 (line)]] | wt | 8.68 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.97× (z +9.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A549 (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.63× (z +11.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[AsPC-1 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -14.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 9.67 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +8.5) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.103× (z -8.5) |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -11.2) |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -12.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -8.9) ⚠ cell-cycle shift, explains ~89% of this change |
| [[NCI-H1792 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -11.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 8.08 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.5 µM 0.0685× (z -10.8) |
| [[SNU-423 (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.4) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[SW1417 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.0) ⚠ cell-cycle shift, explains ~89% of this change |
| [[A-172 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKCD]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[ELOF1]] | +0.62 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[MAP1S]] | +0.60 | +0.36 / +0.68 | both halves | 1e-04 |  |
| [[EMC6]] | +0.60 | +0.20 / +0.68 | both halves | 7e-04 |  |
| [[IL10RB]] | +0.60 | +0.37 / +0.66 | both halves | 8e-05 |  |
| [[DAXX]] | +0.59 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[TNIP2]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SIRT7]] | +0.57 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[DTX2]] | +0.56 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[CHMP1A]] | +0.55 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SMIM29]] | +0.55 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[ZNF593]] | +0.55 | +0.20 / +0.64 | ⚠ one half (not replicated) | 8e-04 |  |
| [[CXorf38]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA3]] | -0.57 | -0.25 / -0.65 | both halves | 4e-04 |  |
| [[PTGR2]] | -0.55 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[EWSR1]] | -0.53 | -0.28 / -0.60 | both halves | 3e-04 |  |
| [[SRSF1]] | -0.51 | -0.26 / -0.58 | both halves | 4e-04 |  |
| [[FAM120A]] | -0.51 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[DHFR]] | -0.50 | -0.07 / -0.60 | ⚠ one half (not replicated) | 0.004 |  |
| [[EMC1]] | -0.50 | -0.26 / -0.56 | both halves | 4e-04 |  |
| [[HNRNPR]] | -0.50 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[ERLIN2]] | -0.49 | -0.21 / -0.54 | both halves | 6e-04 |  |
| [[DDX3X]] | -0.49 | -0.24 / -0.55 | both halves | 5e-04 |  |
| [[HNRNPM]] | -0.49 | -0.23 / -0.55 | both halves | 5e-04 |  |
| [[TAS2R30]] | -0.49 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[LRPPRC]] | -0.49 | -0.33 / -0.58 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.506). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.5, -8.4); signed map (-15.4, -6.6). **Vector** length 79.1, 16.2% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.8 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +3.4 | +3.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.0 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +4.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.8 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.5 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ras homolog family member G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:3,826,978-3,840,959 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC125835, MGC125836; previously ARHG |
| Gene groups (HGNC) | Rho family GTPases |
| Hallmark sets | INFLAMMATORY_RESPONSE, COMPLEMENT |
| Reactome | 18 pathways, smallest: RHO GTPases activate KTN1; GPVI-mediated activation cascade; Constitutive Signaling by Aberrant PI3K in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P84095](https://www.uniprot.org/uniprotkb/P84095) (Rho-related GTP-binding protein RhoG):

> Plays a role in immunological synaptic F-actin density and architecture organization. Regulates actin reorganization in lymphocytes, possibly through the modulation of Rac1 activity. Acts as an activator of the ELMO-DOCK-Rac pathway. Required for the formation of membrane ruffles during macropinocytosis. Plays a role in cell migration and is required for the formation of cup-like structures during trans-endothelial migration of leukocytes. Binds phospholipids in an activation-dependent manner; …

**Summary**, from NCBI Gene [391](https://www.ncbi.nlm.nih.gov/gene/391):

> This gene encodes a member of the Rho family of small GTPases, which cycle between inactive GDP-bound and active GTP-bound states and function as molecular switches in signal transduction cascades. Rho proteins promote reorganization of the actin cytoskeleton and regulate cell shape, attachment, and motility. The encoded protein facilitates translocation of a functional guanine nucleotide exchange factor (GEF) complex from the cytoplasm to the plasma membrane where ras-related C3 botulinum …

**Accessions** — [HGNC:672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:672) · Entrez [391](https://www.ncbi.nlm.nih.gov/gene/391) · UniProt [P84095](https://www.uniprot.org/uniprotkb/P84095) · Ensembl [ENSG00000177105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177105)

## Data

Gene col 10791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10791); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10791]; `tensor/DDL_lfc|DDL_z.npy` [10791]; `embed/gene_vectors.npy` [10791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10791 or target_col == 10791). Every well: [[RHOG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
