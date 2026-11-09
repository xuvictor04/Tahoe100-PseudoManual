---
symbol: "TPT1"
type: "gene"
col: 5419
ensembl_id: "ENSG00000133112"
name: "tumor protein, translationally-controlled 1"
location: "13q14.13"
module: 131
arm: "+"
pooled_cpm: 731.1
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# TPT1

*tumor protein, translationally-controlled 1* — 13q14.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.15× (z +8.7, q 2e-15, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.61× (z +3.7, q 0.020, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Folic acid (drug)]] 5 µM: 0.706× (z -3.8, q 0.089, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL28]] (+0.89, fdr 7e-06), [[RPL32]] (+0.88, fdr 7e-06), [[RPS25]] (+0.87, fdr 7e-06); moves opposite to [[PNPO]] (-0.72, fdr 7e-06), [[DCLRE1A]] (-0.70, fdr 7e-06), [[PPIL1]] (-0.66, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +8.7 | 2e-15 | 49/49 (C-33 A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +7.1 | 3e-10 | 42/44 (SHP-77, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +5.9 | 6e-07 | 43/45 (C-33 A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.20× | +4.8 | 2e-04 | 25/50 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.78×** | +4.5 | 9e-04 | 46/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.76×** | +4.4 | 0.001 | 46/48 (NCI-H460, AsPC-1, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +3.7 | 0.020 | 44/48 (HT-29, A498, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.031 | 40/48 (C32, SHP-77, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.090 | 39/48 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.05× | +3.0 | 0.14 | 46/48 (C-33 A, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5419.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | **0.706×** | -3.8 | 0.089 | 48/48 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.742× | -3.2 | 0.34 | 28/48 (CHP-212, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 807 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.48× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 597 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +10.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 343 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.95× (z +12.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 727 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 1,670 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 238 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.12× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 342 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.91× (z +10.8) | — |
| [[A-172 (line)]] | wt | 433 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 510 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 580 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 461 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 940 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.55× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HEC-1-A (line)]] | alt | 797 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 721 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 365 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 1,367 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 364 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 758 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 1,280 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +10.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 379 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 764 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 839 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 912 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 418 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 331 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 774 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 601 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1,307 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 510 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1,257 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1,048 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 855 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 531 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1,025 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 840 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1,057 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 656 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 733 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 521 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 822 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 487 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 859 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 444 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 502 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 896 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 651 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 857 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 542 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 583 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1,042 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL28]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | STRING 866 |
| [[RPL32]] | +0.88 | +0.85 / +0.86 | both halves | 7e-06 | same gene group; STRING 962 |
| [[RPS25]] | +0.87 | +0.84 / +0.87 | both halves | 7e-06 | STRING 929 |
| [[RPS11]] | +0.86 | +0.83 / +0.87 | both halves | 7e-06 | same gene group; STRING 965 |
| [[RPS16]] ⚠ | +0.86 | +0.82 / +0.86 | both halves | 7e-06 | STRING 962; ⚠ in the vector space only through flagged drug-doses |
| [[RPLP2]] | +0.86 | +0.82 / +0.85 | both halves | 7e-06 | same gene group; STRING 970 |
| [[RPL36A]] | +0.86 | +0.84 / +0.84 | both halves | 7e-06 | STRING 689 |
| [[RPS13]] ⚠ | +0.85 | +0.82 / +0.84 | both halves | 7e-06 | same gene group; STRING 956; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.85 | +0.85 / +0.83 | both halves | 7e-06 | STRING 973 |
| [[RPL38]] | +0.85 | +0.77 / +0.84 | both halves | 7e-06 | STRING 770 |
| [[RPL34]] | +0.85 | +0.81 / +0.83 | both halves | 7e-06 | STRING 823 |
| [[RPL13]] | +0.84 | +0.81 / +0.83 | both halves | 7e-06 | same gene group; STRING 960 |
| [[RPS21]] | +0.84 | +0.77 / +0.87 | both halves | 7e-06 | STRING 838 |
| [[RPS20]] | +0.84 | +0.82 / +0.82 | both halves | 7e-06 | same gene group; STRING 978 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.72 | -0.65 / -0.74 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.70 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[PPIL1]] | -0.66 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[UTP15]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[POGLUT3]] | -0.62 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[MRPL35]] | -0.62 | -0.63 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.871). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-47.0, -27.2); signed map (-62.0, -3.7). **Vector** length 105, 62.6% of its response variance represented; |z| ≥ 3 in 625 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.83 to 20); *Peptide chain elongation* (reactome, mean cos +0.84 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.84 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.9 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +0.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +3.6 | +1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.5 | +2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.4 | +0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.6 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.7 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | tumor protein, translationally-controlled 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.13 — chr13:45,333,471-45,341,284 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TCTP, fortilin |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P13693](https://www.uniprot.org/uniprotkb/P13693) (Translationally-controlled tumor protein):

> Involved in calcium binding and microtubule stabilization. Acts as a negative regulator of TSC22D1-mediated apoptosis, via interaction with and destabilization of TSC22D1 protein.

**Summary**, from NCBI Gene [7178](https://www.ncbi.nlm.nih.gov/gene/7178):

> This gene encodes a protein that is a regulator of cellular growth and proliferation. Its mRNA is highly structured and contains an oligopyrimidine tract (5'-TOP) in its 5' untranslated region that functions to repress its translation under quiescent conditions. The encoded protein is involved in a variety of cellular pathways, including apoptosis, protein synthesis and cell division. It binds to and stabilizes microtubules, and removal of this protein through phosphorylation is required for …

**Accessions** — [HGNC:12022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12022) · Entrez [7178](https://www.ncbi.nlm.nih.gov/gene/7178) · UniProt [P13693](https://www.uniprot.org/uniprotkb/P13693) · Ensembl [ENSG00000133112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133112)

## Data

Gene col 5419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5419); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5419]; `tensor/DDL_lfc|DDL_z.npy` [5419]; `embed/gene_vectors.npy` [5419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5419 or target_col == 5419). Every well: [[TPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
