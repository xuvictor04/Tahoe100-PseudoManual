---
symbol: "RPL23A"
type: "gene"
col: 12559
ensembl_id: "ENSG00000198242"
name: "ribosomal protein L23a"
location: "17q11.2"
module: 43
arm: "+"
pooled_cpm: 90.89
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL23A

*ribosomal protein L23a* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.76× (z +8.6, q 5e-15, up in 43 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.42× (z +5.7, q 2e-06, up in 46 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SW480 4.15×, NCI-H1573 4.74×, Hs 766T 5.05×, MIA PaCa-2 3.80×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 4.26×, NCI-H460 4.23×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 3.71×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.38×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.284×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.190×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL24]] (+0.85, fdr 7e-06), [[RPL13A]] (+0.83, fdr 7e-06), [[RPL35]] (+0.82, fdr 7e-06, ⚠ RPL35 in the vector space only through flagged drug-doses), [[RPL19]] (+0.82, fdr 7e-06); moves opposite to [[SLC35A4]] (-0.64, fdr 1e-05), [[SLC35F6]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12559.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SW480 4.15×, NCI-H1573 4.74×, Hs 766T 5.05×, MIA PaCa-2 3.80×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 4.26×, NCI-H460 4.23×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 3.71×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.38×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.76×** | +8.6 | 5e-15 | 43/44 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.18×** | +8.1 | 2e-13 | 46/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.31×** | +6.8 | 2e-09 | 43/45 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.42×** | +5.7 | 2e-06 | 46/49 (PANC-1, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +5.1 | 4e-05 | 42/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.74×** | +4.9 | 1e-04 | 43/48 (A-172, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.7 | 2e-04 | 37/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.55×** | +3.9 | 0.008 | 40/48 (NCI-H460, LS 180, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.54×** | +3.6 | 0.018 | 35/47 (COLO 205, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.48×** | +3.3 | 0.052 | 30/50 (MIA PaCa-2, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12559.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.284×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.190×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.787× | -3.0 | 0.56 | 24/48 (AsPC-1, HepG2/C3A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 88.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 95.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AsPC-1 (line)]] | alt | 55.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C32 (line)]] | wt | 51.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 75.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.05× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1573 (line)]] | alt | 53.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.74× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2347 (line)]] | alt | 116 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 74.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.71× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SNU-1 (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 96.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 92.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 95.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 107 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 150 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 124 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 119 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 20 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL24]] | +0.85 | +0.81 / +0.84 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13A]] | +0.83 | +0.74 / +0.84 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35]] ⚠ | +0.82 | +0.82 / +0.83 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL19]] | +0.82 | +0.78 / +0.81 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.82 | +0.73 / +0.85 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS24]] | +0.82 | +0.71 / +0.84 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.82 | +0.76 / +0.84 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.81 | +0.81 / +0.78 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL38]] | +0.81 | +0.71 / +0.84 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.81 | +0.77 / +0.82 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36A]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPS15A]] | +0.80 | +0.75 / +0.80 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A4]] | -0.64 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[SLC35F6]] | -0.59 | -0.50 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.814). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.3, -29.0); signed map (-62.0, -5.3). **Vector** length 70.3, 26.7% of its response variance represented; |z| ≥ 3 in 567 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.71 to 19); *Translation initiation complex formation* (reactome, mean cos +0.68 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.68 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +0.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.5 | +0.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.7 | +0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.7 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | +0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L23a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,719,985-28,724,359 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L23A, uL23 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62750](https://www.uniprot.org/uniprotkb/P62750) (Large ribosomal subunit protein uL23):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Binds a specific region on the 26S rRNA. May promote p53/TP53 degradation possibly through the stimulation of MDM2-mediated TP53 polyubiquitination.

**Summary**, from NCBI Gene [6147](https://www.ncbi.nlm.nih.gov/gene/6147):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L23P family of ribosomal proteins. It is located in the cytoplasm. The protein may be one of the target molecules involved in mediating growth inhibition by interferon. In …

**Accessions** — [HGNC:10317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10317) · Entrez [6147](https://www.ncbi.nlm.nih.gov/gene/6147) · UniProt [P62750](https://www.uniprot.org/uniprotkb/P62750) · Ensembl [ENSG00000198242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198242)

## Data

Gene col 12559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12559); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12559]; `tensor/DDL_lfc|DDL_z.npy` [12559]; `embed/gene_vectors.npy` [12559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12559 or target_col == 12559). Every well: [[RPL23A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL23A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
