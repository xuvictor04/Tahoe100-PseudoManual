---
symbol: "RPS6"
type: "gene"
col: 5975
ensembl_id: "ENSG00000137154"
name: "ribosomal protein S6"
location: "9p22.1"
module: 43
arm: "+"
pooled_cpm: 820.86
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPS6

*ribosomal protein S6* — 9p22.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.51× (z +7.4, q 5e-11, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 4.04×, KATO III 3.31×, MIA PaCa-2 4.11×, SW480 3.50×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 4.60×, COLO 205 5.63×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.63×; ⚠ cell-cycle shift, explains ~3% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.369×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL9]] (+0.95, fdr 7e-06, ⚠ RPL9 in the vector space only through flagged drug-doses), [[RPS8]] (+0.95, fdr 7e-06), [[RPS3]] (+0.94, fdr 7e-06, ⚠ RPS3 in the vector space only through flagged drug-doses), [[RPL34]] (+0.94, fdr 7e-06), [[RPL5]] (+0.93, fdr 7e-06); moves opposite to [[PNPO]] (-0.67, fdr 1e-05), [[PSME3]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[COX7C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5975.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 4.04×, KATO III 3.31×, MIA PaCa-2 4.11×, SW480 3.50×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 4.60×, COLO 205 5.63×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.63×; ⚠ cell-cycle shift, explains ~3% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.51×** | +7.4 | 5e-11 | 49/49 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.98×** | +7.4 | 5e-11 | 44/44 (C-33 A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +4.9 | 2e-04 | 44/45 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.8 | 0.019 | 44/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.65×** | +3.5 | 0.049 | 45/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | 1.60× | +3.2 | 0.13 | 37/47 (COLO 205, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5975.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.369×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.706× | -3.2 | 0.89 | 47/48 (SHP-77, SW1417, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 880 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +9.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 512 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +8.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 946 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 1,791 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +8.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 836 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.11× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 684 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.2) ⚠ cell-cycle shift, explains ~3% of this change | — |
| [[SNU-1 (line)]] | wt | 1,137 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.0) |
| [[SW480 (line)]] | alt | 1,141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 374 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 649 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 882 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1,099 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 882 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 399 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 253 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 520 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 914 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 762 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 967 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 848 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1,013 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 839 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 762 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 709 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1,130 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 865 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 731 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1,691 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1,306 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 462 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 513 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 584 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 686 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 403 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 945 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 944 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 786 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1,037 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 382 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1,282 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 546 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 464 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 674 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 935 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 477 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 605 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 849 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1,431 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL9]] ⚠ | +0.95 | +0.93 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | +0.95 | +0.93 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS3]] ⚠ | +0.94 | +0.92 / +0.93 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | +0.94 | +0.90 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPL5]] | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.92 | +0.92 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL37]] ⚠ | +0.92 | +0.87 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS17]] ⚠ | +0.92 | +0.87 / +0.91 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS12]] | +0.91 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL11]] | +0.91 | +0.86 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.91 | +0.85 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36A]] | +0.90 | +0.86 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPL17]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.67 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[PSME3]] | -0.65 | -0.51 / -0.70 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COX7C]] | C | RPS6's natural level strengthens COX7C's drug response | RPS6's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.13; direction not clear | 0.0995 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.938). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.2, -27.9); signed map (-60.0, -4.6). **Vector** length 87.7, 63.6% of its response variance represented; |z| ≥ 3 in 459 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.85 to 34); *oxidative phosphorylation* (hallmark, mean cos +0.64 to 9); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.66 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | -0.1 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.6 | +1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.6 | +0.7 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.4 | -0.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.6 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.3 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | +7.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | -3.7 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -0.4 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.4 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +2.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.2 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.1 — chr9:19,375,715-19,380,236 (-) |
| Ensembl biotype | protein_coding |
| Also known as | S6, eS6 |
| Gene groups (HGNC) | S ribosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 60 pathways, smallest: Protein hydroxylation; mTORC1-mediated signalling; Nuclear events stimulated by ALK signaling in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P62753](https://www.uniprot.org/uniprotkb/P62753) (Small ribosomal subunit protein eS6):

> Component of the 40S small ribosomal subunit. Plays an important role in controlling cell growth and proliferation through the selective translation of particular classes of mRNA. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, …

**Summary**, from NCBI Gene [6194](https://www.ncbi.nlm.nih.gov/gene/6194):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a cytoplasmic ribosomal protein that is a component of the 40S subunit. The protein belongs to the S6E family of ribosomal proteins. It is the major substrate of protein kinases in the ribosome, with subsets of five C-terminal serine residues phosphorylated …

**Accessions** — [HGNC:10429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10429) · Entrez [6194](https://www.ncbi.nlm.nih.gov/gene/6194) · UniProt [P62753](https://www.uniprot.org/uniprotkb/P62753) · Ensembl [ENSG00000137154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137154)

## Data

Gene col 5975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5975); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5975]; `tensor/DDL_lfc|DDL_z.npy` [5975]; `embed/gene_vectors.npy` [5975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5975 or target_col == 5975). Every well: [[RPS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
