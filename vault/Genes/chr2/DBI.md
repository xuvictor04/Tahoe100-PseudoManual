---
symbol: "DBI"
type: "gene"
col: 7892
ensembl_id: "ENSG00000155368"
name: "diazepam binding inhibitor, acyl-CoA binding protein"
location: "2q14.2"
module: 86
arm: "+"
pooled_cpm: 32.68
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# DBI

*diazepam binding inhibitor, acyl-CoA binding protein* — 2q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.05× (z +12.2, q 1e-31, up in 44 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.11× (z +12.1, q 3e-31, up in 46 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.211×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACAT2]] (+0.75, fdr 7e-06), [[ERG28]] (+0.62, fdr 7e-06), [[SCD]] (+0.60, fdr 1e-05); moves opposite to [[DRG2]] (-0.55, fdr 1e-04), [[ZNF473]] (-0.54, fdr 2e-05), [[RRP7A]] (-0.52, fdr 3e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7892.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **5.05×** | +12.2 | 1e-31 | 44/44 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.11×** | +12.1 | 3e-31 | 46/47 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.98×** | +10.0 | 2e-21 | 35/35 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.11×** | +7.9 | 3e-13 | 36/38 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +5.9 | 3e-07 | 39/48 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **2.04×** | +5.4 | 8e-06 | 42/45 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +5.2 | 1e-05 | 33/46 (RKO, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.81×** | +4.3 | 0.001 | 31/47 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.80×** | +4.3 | 0.001 | 36/46 (NCI-H1573, C32, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.002 | 37/48 (NCI-H23, A549, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.66×** | +3.8 | 0.008 | 32/47 (NCI-H460, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +3.3 | 0.046 | 25/47 (A-172, hTERT-HPNE, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.52×** | +3.1 | 0.072 | 25/48 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.072 | 26/48 (AsPC-1, SNU-423, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.077 | 30/48 (hTERT-HPNE, SNU-423, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.53×** | +3.1 | 0.080 | 26/48 (A549, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7892.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.211×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Baicalin (drug)]] 5 µM |  | 0.745× | -3.2 | 0.55 | 28/48 (hTERT-HPNE, KATO III, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.672× | -3.0 | 0.55 | 27/48 (COLO 205, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 51.5 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +12.7) | — |
| [[A498 (line)]] | wt | 59.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +11.5) | — |
| [[A549 (line)]] | wt | 28.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.00× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 20.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.13× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +8.7) | — |
| [[LoVo (line)]] | wt | 24.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.05× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 20.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.45× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 25.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +13.1) | — |
| [[Panc 03.27 (line)]] | alt | 23.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.61× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +10.2) | — |
| [[SW480 (line)]] | alt | 29.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.13× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 36.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.0) | — |
| [[C32 (line)]] | wt | 33.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.0× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[CFPAC-1 (line)]] | alt | 36.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 52.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 28.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 32.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.22× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[J82 (line)]] | alt | 44.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 19.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.95× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.37× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 31.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 40.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.05× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SNU-423 (line)]] | alt | 23.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +9.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 39.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 31.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HepG2_C3A (line)]] | wt | 35.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[KATO III (line)]] | alt | 42.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -8.5) |
| [[LS 180 (line)]] | wt | 49.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.18× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1573 (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.11× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2347 (line)]] | alt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +12.0) | — |
| [[RKO (line)]] | wt | 31.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.67× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW1417 (line)]] | alt | 35.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +9.2) | — |
| [[A-427 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAT2]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 | STRING 592 |
| [[ERG28]] | +0.62 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[SCD]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 447 |
| [[EBP]] | +0.59 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[HMGCR]] | +0.59 | +0.57 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[FDFT1]] | +0.58 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[FDPS]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[LSS]] | +0.57 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[IDI1]] | +0.56 | +0.62 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[PCSK9]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SLC25A1]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SREBF2]] | +0.53 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRG2]] | -0.55 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[ZNF473]] | -0.54 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[RRP7A]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[NLE1]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[PRMT5]] | -0.50 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[DNAJA3]] | -0.50 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[EEFSEC]] | -0.48 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[SRRD]] | -0.47 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[CIAO1]] | -0.46 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[LSG1]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[TATDN1]] | -0.46 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[ACSF3]] | -0.45 | -0.36 / -0.47 | both halves | 9e-05 | pathway: Fatty acid metabolism |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.5, -48.2); signed map (-53.6, 31.8). **Vector** length 83.2, 26.8% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Regulation of cholesterol biosynthesis by SREBP (SREBF)* (reactome, mean cos +0.51 to 17); *Activation of gene expression by SREBF (SREBP)* (reactome, mean cos +0.51 to 16); *Lanosterol biosynthesis* (reactome, mean cos +0.55 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +12.1 |
|  | [[Berbamine (drug)]] 5 µM |  | +4.3 | +4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +5.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.9 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +1.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | +0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | diazepam binding inhibitor, acyl-CoA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.2 — chr2:119,366,924-119,372,550 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACBP, ACBD1 |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [P07108](https://www.uniprot.org/uniprotkb/P07108) (Acyl-CoA-binding protein):

> Binds medium- and long-chain acyl-CoA esters with very high affinity and may function as an intracellular carrier of acyl-CoA esters. It is also able to displace diazepam from the benzodiazepine (BZD) recognition site located on the GABA type A receptor. It is therefore possible that this protein also acts as a neuropeptide to modulate the action of the GABA receptor.

**Summary**, from NCBI Gene [1622](https://www.ncbi.nlm.nih.gov/gene/1622):

> This gene encodes diazepam binding inhibitor, a protein that is regulated by hormones and is involved in lipid metabolism and the displacement of beta-carbolines and benzodiazepines, which modulate signal transduction at type A gamma-aminobutyric acid receptors located in brain synapses. The protein is conserved from yeast to mammals, with the most highly conserved domain consisting of seven contiguous residues that constitute the hydrophobic binding site for medium- and long-chain …

**Accessions** — [HGNC:2690](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2690) · Entrez [1622](https://www.ncbi.nlm.nih.gov/gene/1622) · UniProt [P07108](https://www.uniprot.org/uniprotkb/P07108) · Ensembl [ENSG00000155368](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155368)

## Data

Gene col 7892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7892); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7892]; `tensor/DDL_lfc|DDL_z.npy` [7892]; `embed/gene_vectors.npy` [7892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7892 or target_col == 7892). Every well: [[DBI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DBI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
