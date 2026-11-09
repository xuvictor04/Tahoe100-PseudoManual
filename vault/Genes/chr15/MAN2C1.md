---
symbol: "MAN2C1"
type: "gene"
col: 6404
ensembl_id: "ENSG00000140400"
name: "mannosidase alpha class 2C member 1"
location: "15q24.2"
module: 12
arm: "-"
pooled_cpm: 18.3
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MAN2C1

*mannosidase alpha class 2C member 1* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.11× (z +5.3, q 6e-05, up in 2 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.23× (z +4.5, q 0.002, up in 24 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 3.55×).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.608× (z -10.8, q 1e-24, down in 34 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.647× (z -6.7, q 4e-09, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POMGNT1]] (+0.67, fdr 7e-06), [[LIG3]] (+0.66, fdr 1e-05), [[AKT1]] (+0.62, fdr 7e-06); moves opposite to [[RP9]] (-0.61, fdr 1e-05), [[PIGBOS1]] (-0.59, fdr 1e-05), [[FRG1]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6404.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 3.55×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.3 | 6e-05 | 2/48 (SNU-423, CHP-212) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.5 | 0.002 | 24/46 (AsPC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.037 | 7/48 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.24× | +3.2 | 0.16 | 12/30 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.16 | 4/48 (KATO III, CFPAC-1, …) | top dose only | position effect removed |
| [[Posaconazole (drug)]] 5 µM |  | 1.22× | +3.0 | 0.22 | 5/48 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6404.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.608×** | -10.8 | 1e-24 | 34/47 (Panc 03.27, SNU-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.622×** | -7.0 | 6e-10 | 31/47 (LoVo, LOX-IMVI, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.647×** | -6.7 | 4e-09 | 27/46 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.664×** | -6.3 | 5e-08 | 27/47 (SNU-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.691×** | -5.7 | 2e-06 | 24/47 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.692×** | -5.6 | 2e-06 | 23/45 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.747×** | -4.5 | 6e-04 | 18/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.748×** | -4.5 | 6e-04 | 20/48 (PANC-1, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.764×** | -4.1 | 0.002 | 17/47 (HCT15, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.768×** | -4.0 | 0.003 | 16/48 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.842× | -3.7 | 0.010 | 13/48 (KATO III, C-33 A, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.650×** | -3.5 | 0.025 | 16/48 (KATO III, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.034 | 16/47 (SW48, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.796×** | -3.3 | 0.040 | 17/47 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.676×** | -3.1 | 0.062 | 10/45 (Hs 766T, J82, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.678×** | -3.1 | 0.062 | 5/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | 0.865× | -3.1 | 0.062 | 4/48 (KATO III, HEC-1-A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6404. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 10.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +9.2) | [[Docetaxel (drug)]] 0.05 µM 0.0866× (z -12.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 17.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.356× (z -9.1) |
| [[SW48 (line)]] | wt | 18.4 | 0 | 2 (1 ⚠) | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.112× (z -8.8) |
| [[A549 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0904× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0846× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 13.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0816× (z -10.3) |
| [[J82 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0628× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 26.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -10.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RKO (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -8.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 30.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6404), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POMGNT1]] | +0.67 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[LIG3]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[AKT1]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CHID1]] | +0.60 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[UBE2G2]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[NECAB3]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[KAT2A]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[CERS2]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PGGHG]] | +0.57 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[LENG8]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ARHGAP4]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RP9]] | -0.61 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[FRG1]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ASB8]] | -0.58 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[TCEAL8]] | -0.58 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[SECISBP2L]] | -0.56 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[SEC62]] | -0.55 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[GPATCH11]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[SNRPB2]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[INIP]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[AGGF1]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ISCA2]] | -0.52 | -0.31 / -0.61 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.531). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-20.4, -27.0); signed map (-24.4, -43.6). **Vector** length 71.9, 12.0% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.3 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.1 | +2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | -1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.4 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.0 | -10.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.9 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -5.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -6.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase alpha class 2C member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,355,207-75,368,612 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MANA1, MANA |
| Gene groups (HGNC) | Mannosidases alpha class 2 |
| Reactome | 2 pathways, smallest: Lysosomal oligosaccharide catabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTJ4](https://www.uniprot.org/uniprotkb/Q9NTJ4) (Alpha-mannosidase 2C1):

> Cleaves alpha 1,2-, alpha 1,3-, and alpha 1,6-linked mannose residues on cytoplasmic free oligosaccharides generated by N-glycoprotein degradation pathways.

**Summary**, from NCBI Gene [4123](https://www.ncbi.nlm.nih.gov/gene/4123):

> Predicted to enable alpha-mannosidase activity. Predicted to be involved in oligosaccharide catabolic process. Predicted to be located in cytosol. Implicated in congenital disorder of deglycosylation 2. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6827) · Entrez [4123](https://www.ncbi.nlm.nih.gov/gene/4123) · UniProt [Q9NTJ4](https://www.uniprot.org/uniprotkb/Q9NTJ4) · Ensembl [ENSG00000140400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140400)

## Data

Gene col 6404: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6404); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6404, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6404]; `tensor/DDL_lfc|DDL_z.npy` [6404]; `embed/gene_vectors.npy` [6404]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6404 or target_col == 6404). Every well: [[MAN2C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAN2C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
