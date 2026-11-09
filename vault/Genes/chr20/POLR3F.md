---
symbol: "POLR3F"
type: "gene"
col: 5355
ensembl_id: "ENSG00000132664"
name: "RNA polymerase III subunit F"
location: "20p11.23"
module: 89
arm: "+"
pooled_cpm: 17.37
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# POLR3F

*RNA polymerase III subunit F* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.99× (z +13.5, q 1e-38, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.676× (z -11.5, q 9e-28, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2347 0.226×, KATO III 0.214×, SW 900 0.199×; ⚠ toxic; transcription drop); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (HCT15 0.0712×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.106×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.388×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS33A]] (+0.72, fdr 7e-06), [[IREB2]] (+0.70, fdr 7e-06), [[TEFM]] (+0.69, fdr 7e-06); moves opposite to [[TMSB4X]] (-0.60, fdr 3e-05), [[TFRC]] (-0.55, fdr 1e-05).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.99×** | +13.5 | 1e-38 | 40/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.90×** | +13.3 | 6e-38 | 39/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +12.0 | 4e-31 | 30/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +11.7 | 2e-29 | 37/43 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +11.0 | 6e-26 | 31/46 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.70×** | +11.0 | 6e-26 | 31/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +9.4 | 6e-19 | 35/48 (RKO, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +7.3 | 3e-11 | 23/40 (A498, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +7.1 | 1e-10 | 21/47 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +7.0 | 1e-10 | 25/47 (A498, SW 900, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.40×** | +7.0 | 1e-10 | 25/48 (COLO 205, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.37×** | +6.6 | 2e-09 | 21/48 (AsPC-1, LoVo, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.34×** | +6.0 | 7e-08 | 21/48 (AsPC-1, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +5.8 | 2e-07 | 21/47 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +5.7 | 6e-07 | 18/48 (A498, RKO, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +5.0 | 2e-05 | 14/48 (SNU-423, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.9 | 3e-05 | 21/48 (PANC-1, SW1417, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 4e-04 | 16/48 (KATO III, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.002 | 11/48 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.007 | 10/45 (HCT15, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.007 | 7/46 (NCI-H1792, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5355.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2347 0.226×, KATO III 0.214×, SW 900 0.199×; ⚠ toxic; transcription drop); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (HCT15 0.0712×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.106×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.388×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.676×** | -11.5 | 9e-28 | 39/48 (RPMI-7951, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.653×** | -8.8 | 3e-16 | 28/48 (HCT15, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -6.1 | 2e-07 | 1/48 (H4) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.826×** | -3.8 | 0.019 | 13/30 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.852× | -3.3 | 0.10 | 17/42 (C-33 A, NCI-H2347, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 18.6 | 0 | 2 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0712× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.106× (z -12.0) |
| [[KATO III (line)]] | alt | 20.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -11.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.50× (z +10.1) | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0840× (z -9.9) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -12.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 26.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.9) |
| [[SW 900 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS33A]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[IREB2]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[TEFM]] | +0.69 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[TTF1]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[MRPS11]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ALKBH3]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[POLL]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 | STRING 538 |
| [[GPATCH3]] | +0.67 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[TTC4]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[PAAF1]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[COMMD5]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMSB4X]] | -0.60 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[TFRC]] | -0.55 | -0.54 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.0, 7.4); signed map (-9.3, -17.0). **Vector** length 81.5, 15.1% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +13.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.6 | +13.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +11.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.8 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +11.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.2 | -11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.2 | -8.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.8 | -2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.8 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase III subunit F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:18,466,878-18,484,648 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPC39, RPC6, C34 |
| Gene groups (HGNC) | RNA polymerase subunits; MicroRNA protein coding host genes |
| Reactome | 10 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1D9](https://www.uniprot.org/uniprotkb/Q9H1D9) (DNA-directed RNA polymerase III subunit RPC6):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Specific peripheric component of RNA polymerase III (Pol III) which synthesizes small non-coding RNAs including 5S rRNA, snRNAs, tRNAs and miRNAs from at least 500 distinct genomic loci. Part of POLR3C/RPC3-POLR3F/RPC6-POLR3G/RPC7 heterotrimer that coordinates the dynamics of Pol III stalk and clamp modules during the transition from apo to elongation state. Pol …

**Summary**, from NCBI Gene [10621](https://www.ncbi.nlm.nih.gov/gene/10621):

> The protein encoded by this gene is one of more than a dozen subunits forming eukaryotic RNA polymerase III (RNA Pol III), which transcribes 5S ribosomal RNA and tRNA genes. This protein has been shown to bind both TFIIIB90 and TBP, two subunits of RNA polymerase III transcription initiation factor IIIB (TFIIIB). Unlike most of the other RNA Pol III subunits, the encoded protein is unique to this polymerase. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep …

**Accessions** — [HGNC:15763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15763) · Entrez [10621](https://www.ncbi.nlm.nih.gov/gene/10621) · UniProt [Q9H1D9](https://www.uniprot.org/uniprotkb/Q9H1D9) · Ensembl [ENSG00000132664](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132664)

## Data

Gene col 5355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5355); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5355]; `tensor/DDL_lfc|DDL_z.npy` [5355]; `embed/gene_vectors.npy` [5355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5355 or target_col == 5355). Every well: [[POLR3F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR3F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
