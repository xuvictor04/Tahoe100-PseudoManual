---
symbol: "MOSPD1"
type: "gene"
col: 2189
ensembl_id: "ENSG00000101928"
name: "motile sperm domain containing 1"
location: "Xq26.3"
module: 74
arm: "+"
pooled_cpm: 26.32
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# MOSPD1

*motile sperm domain containing 1* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.96× (z +12.3, q 4e-32, up in 37 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HepG2/C3A 0.239×, SW48 0.423×, AsPC-1 0.378×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW48 0.406×, HepG2/C3A 0.311×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.200×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0894×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (H4 0.126×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BEX4]] (+0.60, fdr 1e-05), [[RPS27L]] (+0.55, fdr 1e-05), [[CCNDBP1]] (+0.54, fdr 3e-05); moves opposite to [[RANBP1]] (-0.51, fdr 1e-05), [[TUBA1B]] (-0.51, fdr 1e-05), [[ZRANB3]] (-0.49, fdr 6e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2189.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +12.3 | 4e-32 | 37/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +11.8 | 2e-29 | 37/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +10.0 | 2e-21 | 32/48 (NCI-H2030, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +8.9 | 1e-16 | 31/47 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +8.8 | 1e-16 | 29/47 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +7.7 | 9e-13 | 32/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +7.7 | 9e-13 | 24/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +7.5 | 3e-12 | 28/44 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +7.3 | 2e-11 | 25/47 (SNU-423, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +5.9 | 2e-07 | 17/48 (A498, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +5.8 | 3e-07 | 19/47 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.1 | 1e-05 | 15/48 (SW1417, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +5.1 | 2e-05 | 16/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 4e-04 | 17/46 (SW480, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +4.4 | 4e-04 | 17/48 (SW480, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.002 | 10/48 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2189.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HepG2/C3A 0.239×, SW48 0.423×, AsPC-1 0.378×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW48 0.406×, HepG2/C3A 0.311×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.200×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0894×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (H4 0.126×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -4.4 | 0.006 | 5/48 (NCI-H23, A549, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.839× | -3.2 | 0.41 | 10/48 (A498, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 141 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.9) |
| [[A498 (line)]] | wt | 53.0 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 56.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.1) |
| [[AN3 CA (line)]] | alt | 30.1 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0894× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +8.5) | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.126× (z -8.5) |
| [[HOP62 (line)]] | alt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0880× (z -10.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 51.9 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.18× (z +8.5) | — |
| [[A-172 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEX4]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[RPS27L]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CCNDBP1]] | +0.54 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[SLC12A6]] | +0.54 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[RALA]] | +0.51 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[YPEL3]] | +0.51 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[UBE2B]] | +0.49 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[PINK1]] | +0.49 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[HEBP2]] | +0.48 | +0.30 / +0.44 | both halves | 2e-04 |  |
| [[BEX2]] | +0.48 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[GOLGA7]] | +0.48 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[PGPEP1]] | +0.48 | +0.35 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP1]] | -0.51 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[TUBA1B]] | -0.51 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ZRANB3]] | -0.49 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[KNTC1]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[GSTCD]] | -0.48 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[CBX5]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TMPO]] | -0.46 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[PRKDC]] | -0.46 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[PLK4]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[FANCD2]] | -0.45 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[HELLS]] | -0.45 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[NUP153]] | -0.45 | -0.44 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.422). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.4, -53.9); signed map (-13.8, 15.4). **Vector** length 86.2, 17.2% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.7 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +7.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.5 | +5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +4.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.9 | -4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.0 | +2.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.9 | -0.9 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | motile sperm domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:134,887,632-134,915,257 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ473B4 |
| Gene groups (HGNC) | Motile sperm domain containing |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJG1](https://www.uniprot.org/uniprotkb/Q9UJG1) (Motile sperm domain-containing protein 1):

> Plays a role in differentiation and/or proliferation of mesenchymal stem cells. Proposed to be involved in epithelial-to-mesenchymal transition (EMT). However, another study suggests that it is not required for EMT or stem cell self-renewal and acts during later stages of differentiation.

**Summary**, from NCBI Gene [56180](https://www.ncbi.nlm.nih.gov/gene/56180):

> Predicted to be involved in negative regulation of transcription by RNA polymerase II and positive regulation of transcription by RNA polymerase II. Predicted to be located in nucleus and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25235) · Entrez [56180](https://www.ncbi.nlm.nih.gov/gene/56180) · UniProt [Q9UJG1](https://www.uniprot.org/uniprotkb/Q9UJG1) · Ensembl [ENSG00000101928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101928)

## Data

Gene col 2189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2189); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2189]; `tensor/DDL_lfc|DDL_z.npy` [2189]; `embed/gene_vectors.npy` [2189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2189 or target_col == 2189). Every well: [[MOSPD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOSPD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
