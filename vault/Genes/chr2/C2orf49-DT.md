---
symbol: "C2orf49-DT"
type: "gene"
col: 15755
ensembl_id: "ENSG00000272994"
name: "C2orf49 divergent transcript"
location: "2q12.2"
module: 35
arm: "+"
pooled_cpm: 4.06
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# C2orf49-DT

*C2orf49 divergent transcript* — 2q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.78× (z +20.8, q 0e+00, up in 40 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.0992×); [[Allantoin (drug)]] 0.05 µM in 1 line (A498 0.107×; ⚠ transcription drop); [[Altretamine (drug)]] 0.05 µM in 1 line (A-172 0.0782×); [[Radotinib (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0860×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2D3-AS1]] (+0.82, fdr 7e-06), [[CCDC90B-AS1]] (+0.78, fdr 1e-05), [[ZFHX2-AS1]] (+0.78, fdr 7e-06).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15755.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.78×** | +20.8 | 0e+00 | 40/41 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **8.40×** | +20.1 | 0e+00 | 45/45 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.44×** | +13.0 | 3e-36 | 11/11 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.47×** | +12.1 | 3e-31 | 36/39 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.16×** | +10.8 | 3e-25 | 23/24 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +10.4 | 2e-23 | 2/4 (PANC-1, A498) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.04×** | +10.1 | 6e-22 | 18/24 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.12×** | +10.0 | 9e-22 | 32/46 (PANC-1, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.20×** | +7.4 | 6e-12 | 28/38 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +6.6 | 2e-09 | 16/45 (A498, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +6.1 | 5e-08 | 15/33 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.20× | +6.1 | 5e-08 | 17/47 (SHP-77, NCI-H1792, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +5.5 | 1e-06 | 20/40 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.33×** | +4.2 | 0.001 | 3/8 (A498, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.58×** | +4.1 | 0.001 | 11/43 (NCI-H1573, SK-MEL-2, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.52×** | +3.7 | 0.007 | 9/45 (A498, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15755.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.0992×); [[Allantoin (drug)]] 0.05 µM in 1 line (A498 0.107×; ⚠ transcription drop); [[Altretamine (drug)]] 0.05 µM in 1 line (A-172 0.0782×); [[Radotinib (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0860×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.683× | -3.5 | 0.25 | 11/41 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.703× | -3.3 | 0.25 | 14/44 (HOP62, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.795× | -3.1 | 0.39 | 6/47 (CHP-212, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.05 | 3 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +9.7) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0992× (z -10.7) |
| [[A498 (line)]] | wt | 4.33 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.69× (z +11.1) | [[Allantoin (drug)]] 0.05 µM 0.107× (z -10.1) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 3.81 | 2 | 1 | [[Auranofin (drug)]] 5 µM 20.0× (z +9.6) | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM 0.0688× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 4.35 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 2.72 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.22× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 5.31 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +8.5) | [[Radotinib (drug)]] 0.5 µM 0.0860× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 4.12 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.81× (z +10.7) | — |
| [[SW480 (line)]] | alt | 5.44 | 2 | 0 | [[Auranofin (drug)]] 5 µM 9.76× (z +12.0) | — |
| [[A-172 (line)]] | wt | 4.13 | 0 | 1 | — | [[Altretamine (drug)]] 0.05 µM 0.0782× (z -8.8) |
| [[A549 (line)]] | wt | 2.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.80× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 2.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.34× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 3.84 | 1 | 0 | [[Auranofin (drug)]] 5 µM 13.3× (z +9.1) | — |
| [[LoVo (line)]] | wt | 5.28 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.9× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 3.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 6.39 | 1 | 0 | [[Auranofin (drug)]] 5 µM 13.5× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 2.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.88× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 8.11 | 1 | 0 | [[Auranofin (drug)]] 5 µM 18.6× (z +11.8) | — |
| [[A-427 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2D3-AS1]] | +0.82 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[CCDC90B-AS1]] | +0.78 | +0.80 / +0.53 | both halves | 1e-05 |  |
| [[ZFHX2-AS1]] | +0.78 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[MZF1-AS1]] | +0.78 | +0.85 / +0.49 | both halves | 1e-05 |  |
| [[ZNF546]] | +0.77 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[PCBP1-AS1]] | +0.77 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[DDX19A-DT]] | +0.77 | +0.75 / +0.58 | both halves | 7e-06 | same gene group |
| [[PBLD]] | +0.76 | +0.78 / +0.41 | both halves | 4e-05 |  |
| [[CIBAR1-DT]] | +0.76 | +0.67 / +0.57 | both halves | 1e-05 | same gene group |
| [[SRRM2-AS1]] | +0.76 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[DENND6A-AS1]] | +0.76 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[PTOV1-AS1]] | +0.76 | +0.69 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C2orf49-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GREB1]] | B | GREB1 activity raises C2orf49-DT's level | lines that do not express GREB1 (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without GREB1 | 0.088 | ⚠ within organs, on part of the lines; also absent: PRKN, SLC17A7, ENSG00000232855; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.787). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.0, 11.9); signed map (22.8, -3.4). **Vector** length 74.0, 12.6% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.5 | +20.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +20.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +13.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +1.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | C2orf49 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q12.2 — chr2:105,333,935-105,337,509 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55178) · Entrez [100506473](https://www.ncbi.nlm.nih.gov/gene/100506473) · Ensembl [ENSG00000272994](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272994)

## Data

Gene col 15755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15755); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15755]; `tensor/DDL_lfc|DDL_z.npy` [15755]; `embed/gene_vectors.npy` [15755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15755 or target_col == 15755). Every well: [[C2orf49-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2orf49-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
